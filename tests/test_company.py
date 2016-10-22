from io import StringIO
import tempfile
from unittest import TestCase

from directory_api_client.company import CompanyAPIClient
from tests import stub_request


class CompanyAPIClientTest(TestCase):

    def setUp(self):
        self.client = CompanyAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/company/details/1/', 'patch')
    def test_update_profile_handles_data(self, stub):
        data = {'key': 'value'}
        self.client.update_profile(id=1, data=data)
        request = stub.request_history[0]
        assert request.json() == data

    @stub_request('https://example.com/company/details/1/', 'patch')
    def test_update_profile_handles_files(self, stub):
        handle, logo_path = tempfile.mkstemp()
        data = {
            'logo': StringIO('hello'),
        }
        self.client.update_profile(id=1, data=data)
        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'filename="logo"\r\n\r\nhello\r\n' in request.text

    @stub_request('https://example.com/company/details/1/', 'patch')
    def test_update_profile_handles_files_and_data(self, stub):
        handle, logo_path = tempfile.mkstemp()
        data = {
            'logo': StringIO('hello'),
            'key': 'value',
        }
        self.client.update_profile(id=1, data=data)
        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'name="key"\r\n\r\nvalue\r\n' in request.text
        assert 'filename="logo"\r\n\r\nhello\r\n' in request.text

    @stub_request('https://example.com/company/details/1/', 'get')
    def test_retrieve_profile(self, stub):
        self.client.retrieve_profile(id=1)

    @stub_request('https://example.com/company/companies-house-profile/',
                  'get')
    def test_retrieve_companies_house_profile(self, stub):
        self.client.retrieve_companies_house_profile('01234567')
        request = stub.request_history[0]
        assert request.query == 'number=01234567'

    @stub_request('https://example.com/validate-company-number/', 'get')
    def test_validate_company_number(self, stub):
        self.client.validate_company_number('01234567')
        request = stub.request_history[0]
        assert request.query == 'number=01234567'

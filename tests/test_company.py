from io import StringIO
import tempfile
from unittest import TestCase

from exportdirectory.company import CompanyAPIClient
from tests import stub_request


class CompanyAPIClientTest(TestCase):

    def setUp(self):
        self.client = CompanyAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/company/1/', 'patch')
    def test_update_profile_handles_data(self, stub):
        data = {'key': 'value'}
        self.client.update_profile(id=1, data=data)
        request = stub.request_history[0]
        assert request.json() == data

    @stub_request('https://example.com/company/1/', 'patch')
    def test_update_profile_handles_files(self, stub):
        handle, logo_path = tempfile.mkstemp()
        data = {
            'logo': open(logo_path, 'rb'),
        }
        self.client.update_profile(id=1, data=data)
        request = stub.request_history[0]

    @stub_request('https://example.com/company/1/', 'patch')
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

    @stub_request('https://example.com/company/1/', 'get')
    def test_retrieve_profile(self, stub):
        self.client.retrieve_profile(id=1)

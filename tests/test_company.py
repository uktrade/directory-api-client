from io import StringIO
from unittest import TestCase

from directory_api_client.company import CompanyAPIClient
from tests import stub_request


class CompanyAPIClientTest(TestCase):

    def setUp(self):
        self.client = CompanyAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/user/1/company/', 'patch')
    def test_update_profile_handles_data(self, stub):
        data = {'key': 'value'}
        self.client.update_profile(sso_user_id=1, data=data)
        request = stub.request_history[0]
        assert request.json() == data

    @stub_request('https://example.com/user/1/company/', 'patch')
    def test_update_profile_handles_files(self, stub):
        data = {
            'logo': StringIO('hello'),
        }
        self.client.update_profile(sso_user_id=1, data=data)
        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'filename="logo"\r\n\r\nhello\r\n' in request.text

    @stub_request('https://example.com/user/1/company/', 'patch')
    def test_update_profile_handles_files_and_data(self, stub):
        data = {
            'logo': StringIO('hello'),
            'key': 'value',
        }
        self.client.update_profile(sso_user_id=1, data=data)
        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'name="key"\r\n\r\nvalue\r\n' in request.text
        assert 'filename="logo"\r\n\r\nhello\r\n' in request.text

    @stub_request('https://example.com/user/1/company/', 'get')
    def test_retrieve_profile(self, stub):
        self.client.retrieve_profile(sso_user_id=1)

    @stub_request('https://example.com/company/public/?page=1', 'get')
    def test_list_public_profile_default_page_number(self, stub):
        self.client.list_public_profiles()

    @stub_request('https://example.com/company/public/?page=4', 'get')
    def test_list_public_profile_specified_page_number(self, stub):
        self.client.list_public_profiles(page=4)

    @stub_request('https://example.com/company/public/1/', 'get')
    def test_retrieve_public_profile_by_companies_house_number(self, stub):
        self.client.retrieve_public_profile_by_companies_house_number(number=1)

    @stub_request('https://example.com/validate/company-number/', 'get')
    def test_validate_company_number(self, stub):
        self.client.validate_company_number('01234567')
        request = stub.request_history[0]
        assert request.query == 'number=01234567'

    @stub_request('https://example.com/user/2/company/case-study/', 'post')
    def test_create_supplier_case_study(self, stub):
        data = {'field': 'value'}
        self.client.create_supplier_case_study(data=data, sso_user_id=2)
        request = stub.request_history[0]
        assert request.json() == data

    @stub_request('https://example.com/user/2/company/case-study/', 'post')
    def test_create_supplier_case_study_handles_files(self, stub):
        data = {
            'image_one': StringIO('_image_one'),
            'image_two': StringIO('_image_two'),
            'image_three': StringIO('_image_three'),
            'video_one': StringIO('_video_one'),
        }
        self.client.create_supplier_case_study(data=data, sso_user_id=2)

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'filename="image_one"\r\n\r\n_image_one\r\n' in request.text
        assert 'filename="image_two"\r\n\r\n_image_two\r\n' in request.text
        assert 'filename="image_three"\r\n\r\n_image_three\r\n' in request.text
        assert 'filename="video_one"\r\n\r\n_video_one\r\n' in request.text

    @stub_request('https://example.com/user/2/company/case-study/', 'post')
    def test_create_supplier_case_study_handles_files_and_data(self, stub):
        data = {
            'image_one': StringIO('_image_one'),
            'image_two': None,
            'field': 'value',
        }
        self.client.create_supplier_case_study(sso_user_id=2, data=data)

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'name="field"\r\n\r\nvalue\r\n' in request.text
        assert 'filename="image_one"\r\n\r\n_image_one\r\n' in request.text

    @stub_request('https://example.com/user/2/company/case-study/1/', 'patch')
    def test_update_supplier_case_study(self, stub):
        data = {'field': 'value'}
        self.client.update_supplier_case_study(
            data=data, sso_user_id=2, case_study_id=1
        )

        request = stub.request_history[0]
        assert request.json() == data

    @stub_request('https://example.com/user/2/company/case-study/1/', 'patch')
    def test_update_supplier_case_study_hanles_files(self, stub):
        data = {
            'image_one': StringIO('_image_one'),
            'image_two': StringIO('_image_two'),
            'image_three': StringIO('_image_three'),
            'video_one': StringIO('_video_one'),
        }
        self.client.update_supplier_case_study(
            data=data, sso_user_id=2, case_study_id=1
        )

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'filename="image_one"\r\n\r\n_image_one\r\n' in request.text
        assert 'filename="image_two"\r\n\r\n_image_two\r\n' in request.text
        assert 'filename="image_three"\r\n\r\n_image_three\r\n' in request.text
        assert 'filename="video_one"\r\n\r\n_video_one\r\n' in request.text

    @stub_request('https://example.com/user/2/company/case-study/1/', 'patch')
    def test_update_supplier_case_study_hanles_files_and_data(self, stub):
        data = {
            'image_one': StringIO('_image_one'),
            'image_two': None,
            'field': 'value',
        }
        self.client.update_supplier_case_study(
            data=data, sso_user_id=2, case_study_id=1
        )

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'name="field"\r\n\r\nvalue\r\n' in request.text
        assert 'filename="image_one"\r\n\r\n_image_one\r\n' in request.text

    @stub_request('https://example.com/user/2/company/case-study/1/', 'delete')
    def test_delete_supplier_case_study(self, stub):
        self.client.delete_supplier_case_study(sso_user_id=2, case_study_id=1)

    @stub_request('https://example.com/user/2/company/case-study/1/', 'get')
    def retrieve_supplier_case_study(self, stub):
        self.client.retrieve_supplier_case_study(
            sso_user_id=2, case_study_id=1
        )

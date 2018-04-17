from io import StringIO
from unittest import TestCase

from directory_api_client.company import CompanyAPIClient
from tests import stub_request


class CompanyAPIClientTest(TestCase):

    def setUp(self):
        self.client = CompanyAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/supplier/company/', 'patch')
    def test_update_profile_handles_data(self, stub):
        data = {'key': 'value'}
        self.client.update_profile(sso_session_id=1, data=data)

        request = stub.request_history[0]
        assert request.json() == data
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://example.com/supplier/company/', 'patch')
    def test_update_profile_handles_files(self, stub):
        data = {
            'logo': StringIO('hello'),
        }
        self.client.update_profile(sso_session_id=1, data=data)

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'filename="logo"\r\n\r\nhello\r\n' in request.text
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://example.com/supplier/company/', 'patch')
    def test_update_profile_handles_files_and_data(self, stub):
        data = {
            'logo': StringIO('hello'),
            'key': 'value',
        }
        self.client.update_profile(sso_session_id=1, data=data)

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'name="key"\r\n\r\nvalue\r\n' in request.text
        assert 'filename="logo"\r\n\r\nhello\r\n' in request.text
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://example.com/supplier/company/', 'get')
    def test_retrieve_private_profile(self, stub):
        self.client.retrieve_private_profile(sso_session_id=1)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://example.com/public/company/', 'get')
    def test_list_public_profile_no_params(self, stub):
        self.client.list_public_profiles()

    @stub_request('https://example.com/public/company/?page=4', 'get')
    def test_list_public_profile_specified_page_number(self, stub):
        self.client.list_public_profiles(page=4)

    @stub_request(
        'https://example.com/public/company/?page=4&sectors=THING', 'get'
    )
    def test_list_public_profile_multiple_kwargs(self, stub):
        self.client.list_public_profiles(page=4, sectors='THING')

    @stub_request(
        'https://example.com/public/company/?page=4&sectors=1&sectors=2', 'get'
    )
    def test_list_public_profile_multiple_sectors(self, stub):
        self.client.list_public_profiles(page=4, sectors=['1', '2'])

    @stub_request('https://example.com/public/company/1/', 'get')
    def test_retrieve_public_profile(self, stub):
        self.client.retrieve_public_profile(number=1)

    @stub_request('https://example.com/contact/supplier/', 'post')
    def test_send_email(self, stub):
        data = {'body': 'Hello there!'}
        self.client.send_email(data=data)
        request = stub.request_history[0]
        assert request.json() == data

    @stub_request('https://example.com/validate/company-number/', 'get')
    def test_validate_company_number(self, stub):
        self.client.validate_company_number('01234567')
        request = stub.request_history[0]
        assert request.query == 'number=01234567'

    @stub_request('https://example.com/supplier/company/case-study/', 'post')
    def test_create_case_study(self, stub):
        data = {'field': 'value'}
        self.client.create_case_study(data=data, sso_session_id=2)

        request = stub.request_history[0]
        assert request.json() == data
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request('https://example.com/supplier/company/case-study/', 'post')
    def test_create_case_study_handles_files(self, stub):
        data = {
            'image_one': StringIO('_image_one'),
            'image_two': StringIO('_image_two'),
            'image_three': StringIO('_image_three'),
            'video_one': StringIO('_video_one'),
        }
        self.client.create_case_study(data=data, sso_session_id=2)

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'filename="image_one"\r\n\r\n_image_one\r\n' in request.text
        assert 'filename="image_two"\r\n\r\n_image_two\r\n' in request.text
        assert 'filename="image_three"\r\n\r\n_image_three\r\n' in request.text
        assert 'filename="video_one"\r\n\r\n_video_one\r\n' in request.text
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request('https://example.com/supplier/company/case-study/', 'post')
    def test_create_case_study_handles_files_and_data(self, stub):
        data = {
            'image_one': StringIO('_image_one'),
            'image_two': None,
            'field': 'value',
        }
        self.client.create_case_study(sso_session_id=2, data=data)

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'name="field"\r\n\r\nvalue\r\n' in request.text
        assert 'filename="image_one"\r\n\r\n_image_one\r\n' in request.text
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/case-study/1/', 'patch'
    )
    def test_update_case_study(self, stub):
        data = {'field': 'value'}
        self.client.update_case_study(
            data=data, sso_session_id=2, case_study_id=1
        )

        request = stub.request_history[0]
        assert request.json() == data

    @stub_request(
        'https://example.com/supplier/company/case-study/1/', 'patch'
    )
    def test_update_case_study_hanles_files(self, stub):
        data = {
            'image_one': StringIO('_image_one'),
            'image_two': StringIO('_image_two'),
            'image_three': StringIO('_image_three'),
            'video_one': StringIO('_video_one'),
        }
        self.client.update_case_study(
            data=data, sso_session_id=2, case_study_id=1
        )

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'filename="image_one"\r\n\r\n_image_one\r\n' in request.text
        assert 'filename="image_two"\r\n\r\n_image_two\r\n' in request.text
        assert 'filename="image_three"\r\n\r\n_image_three\r\n' in request.text
        assert 'filename="video_one"\r\n\r\n_video_one\r\n' in request.text
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/case-study/1/', 'patch'
    )
    def test_update_case_study_hanles_files_and_data(self, stub):
        data = {
            'image_one': StringIO('_image_one'),
            'image_two': None,
            'field': 'value',
        }
        self.client.update_case_study(
            data=data, sso_session_id=2, case_study_id=1
        )

        request = stub.request_history[0]
        assert 'Content-Disposition: form-data;' in request.text
        assert 'name="field"\r\n\r\nvalue\r\n' in request.text
        assert 'filename="image_one"\r\n\r\n_image_one\r\n' in request.text
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/case-study/1/', 'delete'
    )
    def test_delete_case_study(self, stub):
        self.client.delete_case_study(sso_session_id=2, case_study_id=1)

    @stub_request(
        'https://example.com/supplier/company/case-study/1/', 'get'
    )
    def test_retrieve_private_case_study(self, stub):
        self.client.retrieve_private_case_study(
            sso_session_id=2, case_study_id=1
        )

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request('https://example.com/public/case-study/1/', 'get')
    def test_retrieve_public_case_study(self, stub):
        self.client.retrieve_public_case_study(case_study_id=1)

    @stub_request('https://example.com/supplier/company/verify/', 'post')
    def test_verify_with_code(self, stub):
        self.client.verify_with_code(
            sso_session_id=2, code='222222'
        )

        request = stub.request_history[0]
        assert request.json() == {'code': '222222'}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/verify/companies-house/', 'post'
    )
    def test_verify_with_companies_house(self, stub):
        self.client.verify_with_companies_house(
            sso_session_id=2, access_token='222222'
        )

        request = stub.request_history[0]
        assert request.json() == {'access_token': '222222'}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request('https://example.com/company/search/', 'get')
    def test_search_company(self, stub):
        self.client.search_company(
            term='thing',
            page=1,
            size=10,
            sectors=['AIRPORTS', 'AEROSPACE'],
            campaign_tag='food-is-great',
        )

        request = stub.request_history[0]

        assert 'size=10' in request.url
        assert 'page=1' in request.url
        assert 'term=thing' in request.url
        assert 'sectors=AIRPORTS' in request.url
        assert 'sectors=AEROSPACE' in request.url
        assert 'campaign_tag=food-is-great' in request.url

    @stub_request('https://example.com/case-study/search/', 'get')
    def test_search_case_study(self, stub):
        self.client.search_case_study(
            term='thing',
            page=1,
            size=10,
            sectors=['AIRPORTS', 'AEROSPACE'],
            campaign_tag='food-is-great',
        )

        request = stub.request_history[0]

        assert 'size=10' in request.url
        assert 'page=1' in request.url
        assert 'term=thing' in request.url
        assert 'sectors=AIRPORTS' in request.url
        assert 'sectors=AEROSPACE' in request.url
        assert 'campaign_tag=food-is-great' in request.url

    @stub_request(
        'https://example.com/supplier/company/transfer-ownership-invite/',
        'post'
    )
    def test_create_transfer_invite(self, stub):
        self.client.create_transfer_invite(
            sso_session_id=2, new_owner_email='test@example.com'
        )

        request = stub.request_history[0]
        assert request.json() == {'new_owner_email': 'test@example.com'}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/transfer-ownership-invite/123/',
        'get'
    )
    def test_retrieve_transfer_invite(self, stub):
        self.client.retrieve_transfer_invite(
            sso_session_id=2, invite_key='123'
        )

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/transfer-ownership-invite/123/',
        'patch'
    )
    def test_accept_transfer_invite(self, stub):
        self.client.accept_transfer_invite(
            sso_session_id=2, invite_key='123'
        )

        request = stub.request_history[0]
        assert request.json() == {'accepted': True}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/collaboration-invite/',
        'post'
    )
    def test_create_collaboration_invite(self, stub):
        self.client.create_collaboration_invite(
            sso_session_id=2, collaborator_email='test@example.com'
        )

        request = stub.request_history[0]
        assert request.json() == {'collaborator_email': 'test@example.com'}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/collaboration-invite/123/',
        'get'
    )
    def test_retrieve_collaboration_invite(self, stub):
        self.client.retrieve_collaboration_invite(
            sso_session_id=2, invite_key='123'
        )

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/collaboration-invite/123/',
        'patch'
    )
    def test_accept_collaboration_invite(self, stub):
        self.client.accept_collaboration_invite(
            sso_session_id=2, invite_key='123'
        )

        request = stub.request_history[0]
        assert request.json() == {'accepted': True}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request(
        'https://example.com/supplier/company/remove-collaborators/',
        'post'
    )
    def test_remove_collaborators(self, stub):
        self.client.remove_collaborators(
            sso_session_id=2, sso_ids=[1, 2, 3]
        )

        request = stub.request_history[0]
        assert request.json() == {'sso_ids': [1, 2, 3]}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    @stub_request('https://example.com/supplier/company/collaborators/', 'get')
    def test_retrieve_collaborators(self, stub):
        self.client.retrieve_collaborators(sso_session_id=2)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

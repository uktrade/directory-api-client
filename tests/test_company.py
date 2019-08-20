from io import StringIO

import pytest

from directory_api_client.company import CompanyAPIClient


@pytest.fixture
def client():
    return CompanyAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_update_profile_handles_data(requests_mock, client):
    url = 'https://example.com/supplier/company/'
    requests_mock.patch(url)
    data = {'key': 'value'}
    client.update_profile(sso_session_id=1, data=data)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == data
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 1'


def test_update_profile_handles_files(requests_mock, client):
    url = 'https://example.com/supplier/company/'
    requests_mock.patch(url)

    client.update_profile(sso_session_id=1, data={'logo': StringIO('hello')})

    assert requests_mock.last_request.url == url
    assert 'Content-Disposition: form-data;' in requests_mock.last_request.text
    assert 'filename="logo"\r\n\r\nhello\r\n' in requests_mock.last_request.text
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 1'


def test_update_profile_handles_files_and_data(requests_mock, client):
    url = 'https://example.com/supplier/company/'
    requests_mock.patch(url)

    data = {
        'logo': StringIO('hello'),
        'key': 'value',
    }
    client.update_profile(sso_session_id=1, data=data)

    assert requests_mock.last_request.url == url
    assert 'Content-Disposition: form-data;' in requests_mock.last_request.text
    assert 'name="key"\r\n\r\nvalue\r\n' in requests_mock.last_request.text
    assert 'filename="logo"\r\n\r\nhello\r\n' in requests_mock.last_request.text
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 1'


def test_retrieve_private_profile(requests_mock, client):
    url = 'https://example.com/supplier/company/'
    requests_mock.get(url)

    client.retrieve_private_profile(sso_session_id=1)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 1'


def test_retrieve_public_profile(requests_mock, client):
    url = 'https://example.com/public/company/1/'
    requests_mock.get(url)

    client.retrieve_public_profile(number=1)

    assert requests_mock.last_request.url == url


def test_validate_company_number(requests_mock, client):
    url = 'https://example.com/validate/company-number/'
    requests_mock.get(url)

    client.validate_company_number('01234567')

    assert requests_mock.last_request.url.startswith(url)
    assert requests_mock.last_request.query == 'number=01234567'


def test_create_case_study(requests_mock, client):
    url = 'https://example.com/supplier/company/case-study/'
    requests_mock.post(url)

    data = {'field': 'value'}
    client.create_case_study(data=data, sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == data
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_create_case_study_handles_files(requests_mock, client):
    url = 'https://example.com/supplier/company/case-study/'
    requests_mock.post(url)

    data = {
        'image_one': StringIO('_image_one'),
        'image_two': StringIO('_image_two'),
        'image_three': StringIO('_image_three'),
        'video_one': StringIO('_video_one'),
    }
    client.create_case_study(data=data, sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert 'Content-Disposition: form-data;' in requests_mock.last_request.text
    assert 'filename="image_one"\r\n\r\n_image_one\r\n' in requests_mock.last_request.text
    assert 'filename="image_two"\r\n\r\n_image_two\r\n' in requests_mock.last_request.text
    assert 'filename="image_three"\r\n\r\n_image_three\r\n' in requests_mock.last_request.text
    assert 'filename="video_one"\r\n\r\n_video_one\r\n' in requests_mock.last_request.text
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_create_case_study_handles_files_and_data(requests_mock, client):
    url = 'https://example.com/supplier/company/case-study/'
    requests_mock.post(url)

    data = {
        'image_one': StringIO('_image_one'),
        'image_two': None,
        'field': 'value',
    }
    client.create_case_study(sso_session_id=2, data=data)

    assert requests_mock.last_request.url == url
    assert 'Content-Disposition: form-data;' in requests_mock.last_request.text
    assert 'name="field"\r\n\r\nvalue\r\n' in requests_mock.last_request.text
    assert 'filename="image_one"\r\n\r\n_image_one\r\n' in requests_mock.last_request.text
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_update_case_study(requests_mock, client):
    url = 'https://example.com/supplier/company/case-study/1/'
    requests_mock.patch(url)

    data = {'field': 'value'}
    client.update_case_study(data=data, sso_session_id=2, case_study_id=1)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == data


def test_update_case_study_hanles_files(requests_mock, client):
    url = 'https://example.com/supplier/company/case-study/1/'
    requests_mock.patch(url)

    data = {
        'image_one': StringIO('_image_one'),
        'image_two': StringIO('_image_two'),
        'image_three': StringIO('_image_three'),
        'video_one': StringIO('_video_one'),
    }
    client.update_case_study(data=data, sso_session_id=2, case_study_id=1)

    assert requests_mock.last_request.url == url
    assert 'Content-Disposition: form-data;' in requests_mock.last_request.text
    assert 'filename="image_one"\r\n\r\n_image_one\r\n' in requests_mock.last_request.text
    assert 'filename="image_two"\r\n\r\n_image_two\r\n' in requests_mock.last_request.text
    assert 'filename="image_three"\r\n\r\n_image_three\r\n' in requests_mock.last_request.text
    assert 'filename="video_one"\r\n\r\n_video_one\r\n' in requests_mock.last_request.text
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_update_case_study_hanles_files_and_data(requests_mock, client):
    url = 'https://example.com/supplier/company/case-study/1/'
    requests_mock.patch(url)

    data = {
        'image_one': StringIO('_image_one'),
        'image_two': None,
        'field': 'value',
    }
    client.update_case_study(data=data, sso_session_id=2, case_study_id=1)

    assert requests_mock.last_request.url == url
    assert 'Content-Disposition: form-data;' in requests_mock.last_request.text
    assert 'name="field"\r\n\r\nvalue\r\n' in requests_mock.last_request.text
    assert 'filename="image_one"\r\n\r\n_image_one\r\n' in requests_mock.last_request.text
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_delete_case_study(requests_mock, client):
    url = 'https://example.com/supplier/company/case-study/1/'
    requests_mock.delete(url)

    client.delete_case_study(sso_session_id=2, case_study_id=1)

    assert requests_mock.last_request.url == url


def test_retrieve_private_case_study(requests_mock, client):
    url = 'https://example.com/supplier/company/case-study/1/'
    requests_mock.get(url)

    client.retrieve_private_case_study(sso_session_id=2, case_study_id=1)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_retrieve_public_case_study(requests_mock, client):
    url = 'https://example.com/public/case-study/1/'
    requests_mock.get(url)

    client.retrieve_public_case_study(case_study_id=1)

    assert requests_mock.last_request.url == url


def test_verify_with_code(requests_mock, client):
    url = 'https://example.com/supplier/company/verify/'
    requests_mock.post(url)

    client.verify_with_code(sso_session_id=2, code='222222')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'code': '222222'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_verify_with_companies_house(requests_mock, client):
    url = 'https://example.com/supplier/company/verify/companies-house/'
    requests_mock.post(url)

    client.verify_with_companies_house(sso_session_id=2, access_token='222222')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'access_token': '222222'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_search_find_a_supplier(requests_mock, client):
    url = 'https://example.com/company/search/'
    requests_mock.get(url)

    client.search_find_a_supplier(
        term='thing',
        page=1,
        size=10,
        sectors=['AIRPORTS', 'AEROSPACE'],
        campaign_tag='food-is-great',
    )

    assert requests_mock.last_request.url.startswith(url)
    assert 'size=10' in requests_mock.last_request.url
    assert 'page=1' in requests_mock.last_request.url
    assert 'term=thing' in requests_mock.last_request.url
    assert 'sectors=AIRPORTS' in requests_mock.last_request.url
    assert 'sectors=AEROSPACE' in requests_mock.last_request.url
    assert 'campaign_tag=food-is-great' in requests_mock.last_request.url


def test_search_investment_support_directory(requests_mock, client):
    url = 'https://example.com/investment-support-directory/search/'
    requests_mock.get(url)

    client.search_investment_search_directory(
        term='thing',
        page=1,
        size=10,
        expertise_industries=['REG', 'IT'],
        expertise_languages=['ENGLISH', 'GERMAN', 'SPANISH'],
    )

    assert requests_mock.last_request.url.startswith(url)
    assert 'size=10' in requests_mock.last_request.url
    assert 'page=1' in requests_mock.last_request.url
    assert 'term=thing' in requests_mock.last_request.url
    assert 'expertise_industries=REG' in requests_mock.last_request.url
    assert 'expertise_industries=IT' in requests_mock.last_request.url
    assert 'expertise_languages=ENGLISH' in requests_mock.last_request.url
    assert 'expertise_languages=GERMAN' in requests_mock.last_request.url
    assert 'expertise_languages=SPANISH' in requests_mock.last_request.url


def test_create_transfer_invite(requests_mock, client):
    url = 'https://example.com/supplier/company/transfer-ownership-invite/'
    requests_mock.post(url)

    client.create_transfer_invite(sso_session_id=2, new_owner_email='test@example.com')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'new_owner_email': 'test@example.com'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_retrieve_transfer_invite(requests_mock, client):
    url = 'https://example.com/supplier/company/transfer-ownership-invite/123/'
    requests_mock.get(url)

    client.retrieve_transfer_invite(sso_session_id=2, invite_key='123')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_accept_transfer_invite(requests_mock, client):
    url = 'https://example.com/supplier/company/transfer-ownership-invite/123/'
    requests_mock.patch(url)

    client.accept_transfer_invite(sso_session_id=2, invite_key='123')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'accepted': True}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_create_collaboration_invite(requests_mock, client):
    url = 'https://example.com/supplier/company/collaboration-invite/'
    requests_mock.post(url)

    client.create_collaboration_invite(sso_session_id=2, collaborator_email='test@example.com')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'collaborator_email': 'test@example.com'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_retrieve_collaboration_invite(requests_mock, client):
    url = 'https://example.com/supplier/company/collaboration-invite/123/'
    requests_mock.get(url)

    client.retrieve_collaboration_invite(sso_session_id=2, invite_key='123')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_accept_collaboration_invite(requests_mock, client):
    url = 'https://example.com/supplier/company/collaboration-invite/123/'
    requests_mock.patch(url)

    client.accept_collaboration_invite(sso_session_id=2, invite_key='123')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'accepted': True}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_remove_collaborators(requests_mock, client):
    url = 'https://example.com/supplier/company/remove-collaborators/'
    requests_mock.post(url)

    client.remove_collaborators(sso_session_id=2, sso_ids=[1, 2, 3])

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'sso_ids': [1, 2, 3]}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_retrieve_collaborators(requests_mock, client):
    url = 'https://example.com/supplier/company/collaborators/'
    requests_mock.get(url)

    client.retrieve_collaborators(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_request_collaboration(requests_mock, client):
    url = 'https://example.com/supplier/company/collaborator-request/'
    requests_mock.post(url)

    client.request_collaboration(company_number='1234567', collaborator_email='test@example.com')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {
        'company_number': '1234567',
        'collaborator_email': 'test@example.com',
    }


def test_verify_identity_request(requests_mock, client):
    url = 'https://example.com/supplier/company/verify/identity/'
    requests_mock.post(url)

    client.verify_identity_request(sso_session_id=2)

    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'
    assert requests_mock.last_request.url == url


def test_register_new_member(requests_mock, client):
    url = 'https://example.com/supplier/company/add-new-collaborator/'
    requests_mock.post(url)

    data = {
        'company_number': '1234567',
        'sso_id': '123',
        'company_email': 'abc@def.com',
        'name': 'Abc def',
        'mobile_number': 9876543210,
    }

    client.register_new_collaborator(data)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {
        'company_number': '1234567',
        'sso_id': '123',
        'company_email': 'abc@def.com',
        'name': 'Abc def',
        'mobile_number': 9876543210,
    }

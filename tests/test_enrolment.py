import pytest

from directory_api_client.enrolment import EnrolmentAPIClient


@pytest.fixture
def client():
    return EnrolmentAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_send_form(client, requests_mock):
    url = 'https://example.com/enrolment/'
    requests_mock.post(url)

    client.send_form(form_data='form_data')

    assert requests_mock.last_request.url == url


def test_claim_prepeveried_company(client, requests_mock):
    url = 'https://example.com/enrolment/preverified-company/123/claim/'
    requests_mock.post(url)

    data = {'name': 'Foo Bar'}
    client.claim_prepeveried_company(
        sso_session_id='2',
        key='123',
        data=data,
    )

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == data
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_retrieve_prepeveried_company(client, requests_mock):
    url = 'https://example.com/enrolment/preverified-company/123/'
    requests_mock.get(url)

    client.retrieve_prepeveried_company(key='123')

    assert requests_mock.last_request.url == url

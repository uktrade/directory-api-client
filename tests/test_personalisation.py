import pytest

from directory_api_client.personalisation import PersonalisationAPIClient


@pytest.fixture
def client():
    return PersonalisationAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_personalisation_create(requests_mock, client):
    url = 'https://example.com/personalisation/user-location/'
    requests_mock.post(url)
    data = {}
    client.user_location_create(sso_session_id=2, data=data)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == data
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'

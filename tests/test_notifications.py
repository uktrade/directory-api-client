import pytest

from directory_api_client.notifications import NotificationsAPIClient


@pytest.fixture
def client():
    return NotificationsAPIClient(
        base_url='https://e.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_anonymous_unsubscribe(client, requests_mock):
    url = 'https://e.com/notifications/anonymous-unsubscribe/'
    requests_mock.post(url)

    client.anonymous_unsubscribe(uidb64='aBcDe', token='1a2b3c')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'uidb64': 'aBcDe', 'token': '1a2b3c'}

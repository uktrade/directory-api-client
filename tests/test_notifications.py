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

    client.anonymous_unsubscribe(signed_email_address='a@b.com:1234')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'email': 'a@b.com:1234'}

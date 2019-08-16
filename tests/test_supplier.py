import pytest

from directory_api_client.supplier import SupplierAPIClient


@pytest.fixture
def client():
    return SupplierAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_update_profile(client, requests_mock):
    url = 'https://example.com/supplier/'
    requests_mock.patch(url)

    data = {'key': 'value'}
    client.update_profile(sso_session_id=1, data=data)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == data
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 1'


def test_retrieve_profile(client, requests_mock):
    url = 'https://example.com/supplier/'
    requests_mock.get(url)

    client.retrieve_profile(sso_session_id=1)

    assert requests_mock.last_request.url == url


def test_unsubscribe(client, requests_mock):
    url = 'https://example.com/supplier/unsubscribe/'
    requests_mock.post(url)

    client.unsubscribe(sso_session_id=1)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 1'


def test_get_csv_dump(client, requests_mock):
    url = 'https://example.com/supplier/csv-dump/'
    requests_mock.get(url)

    token = 'debug'
    client.get_csv_dump(token)

    assert requests_mock.last_request.url.startswith(url)
    assert requests_mock.last_request.qs == {'token': ['debug']}

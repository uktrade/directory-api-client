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


def test_personalisation_events_by_location_list(requests_mock, client):
    url = 'https://example.com/personalisation/events/?lat=&lng='
    requests_mock.get(url)
    client.events_by_location_list(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_personalisation_export_opportunities_by_relevance_list(requests_mock, client):
    url = 'https://example.com/personalisation/export-opportunities/?s='
    requests_mock.get(url)
    client.export_opportunities_by_relevance_list(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'

    url = 'https://example.com/personalisation/export-opportunities/?s=food-and-drink'
    requests_mock.get(url)
    client.export_opportunities_by_relevance_list(sso_session_id=2, search_term="food-and-drink")

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_recommended_countries_by_sector(requests_mock, client):
    url = 'https://example.com/personalisation/recommended-countries/?sector=Food'
    requests_mock.get(url)
    sector = {'Food'}
    client.recommended_countries_by_sector(sso_session_id=2, sector=sector)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_get_user_products(requests_mock, client):
    url = 'https://example.com/personalisation/user-products/'
    requests_mock.get(url)

    client.get_user_products(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_get_user_markets(requests_mock, client):
    url = 'https://example.com/personalisation/user-markets/'
    requests_mock.get(url)

    client.get_user_markets(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_add_update_user_product(requests_mock, client):
    url = 'https://example.com/personalisation/user-products/'
    requests_mock.post(url)
    data = {'my_product': 'sample'}
    client.add_update_user_product(sso_session_id=2, data=data)
    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == data
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_add_update_user_market(requests_mock, client):
    url = 'https://example.com/personalisation/user-markets/'
    requests_mock.post(url)
    data = {'my_market': 'sample'}
    client.add_update_user_market(sso_session_id=2, data=data)
    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == data
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'

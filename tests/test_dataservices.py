import pytest

from directory_api_client.dataservices import DataServicesAPIClient


@pytest.fixture
def client():
    return DataServicesAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_get_corruption_perceptions_index(client, requests_mock):
    url = 'https://example.com/dataservices/corruption-perceptions-index/CHN/'
    requests_mock.get(url)
    client.get_corruption_perceptions_index(country_code='CHN')

    assert requests_mock.last_request.url == url


def test_get_easeofdoingbusiness(client, requests_mock):
    url = 'https://example.com/dataservices/easeofdoingbusiness/CHN/'
    requests_mock.get(url)
    client.get_easeofdoingbusiness(country_code='CHN')

    assert requests_mock.last_request.url == url

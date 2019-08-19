import pytest

from directory_api_client.exporting import ExportingAPIClient


@pytest.fixture
def client():
    return ExportingAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_lookup_regional_offices_by_postcode(client, requests_mock):
    url = 'https://example.com/exporting/offices/ABC%20123/'
    requests_mock.get(url)

    client.lookup_regional_offices_by_postcode(postcode='ABC 123')

    assert requests_mock.last_request.url == url

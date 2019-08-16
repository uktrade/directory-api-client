import pytest

from directory_api_client.buyer import BuyerAPIClient


@pytest.fixture
def client():
    return BuyerAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_send_form(client, requests_mock):
    requests_mock.post('https://example.com/buyer/')

    form_data = {'field': 'value'}

    client.send_form(form_data)

    assert requests_mock.last_request.json() == form_data


def test_get_csv_dump(client, requests_mock):
    requests_mock.get('https://example.com/buyer/csv-dump/')

    token = 'debug'
    client.get_csv_dump(token)

    assert requests_mock.last_request.qs == {'token': [token]}

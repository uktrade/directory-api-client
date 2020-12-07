import base64

import pytest

from directory_api_client.testapiclient import DirectoryTestAPIClient


@pytest.fixture
def client():
    return DirectoryTestAPIClient(
        base_url='http://test.uk',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


class BasicAuthenticator:
    def __init__(self, username: str, password: str):
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode("ascii"))
        self.headers = {"Authorization": f"Basic {encoded_credentials.decode('ascii')}"}


@pytest.fixture
def basic_authenticator():
    return BasicAuthenticator("user", "password")


def test_get_company_by_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/12345678/'
    requests_mock.get(url)

    client.get_company_by_ch_id(ch_id='12345678')

    assert requests_mock.last_request.url == url


def test_get_company_should_return_404_on_missing_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/None/'
    requests_mock.get(url, status_code=404)

    client.get_company_by_ch_id(ch_id=None)

    assert requests_mock.last_request.url == url


def test_get_company_should_return_404_on_empty_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/'
    requests_mock.get(url, status_code=404)

    client.get_company_by_ch_id(ch_id='')

    assert requests_mock.last_request.url == url


def test_get_company_should_make_request_on_empty_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/'
    requests_mock.get(url)

    client.get_company_by_ch_id(ch_id='')

    assert requests_mock.last_request.url == url


def test_get_company_should_make_request_on_no_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/None/'
    requests_mock.get(url)

    client.get_company_by_ch_id(ch_id=None)

    assert requests_mock.last_request.url == url


def test_get_company(client, requests_mock):
    url = 'http://test.uk/testapi/company/12345678/'
    requests_mock.get(url)

    client.get_company_by_ch_id(ch_id='12345678')

    assert requests_mock.last_request.url == url


def test_delete_company_by_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/ch_ID_00/'
    requests_mock.delete(url)

    client.delete_company_by_ch_id(ch_id='ch_ID_00')

    assert requests_mock.last_request.url == url


def test_delete_company_should_return_404_on_missing_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/None/'
    requests_mock.delete(url, status_code=404)

    client.delete_company_by_ch_id(ch_id=None)

    assert requests_mock.last_request.url == url


def test_delete_company_should_return_404_on_empty_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/'
    requests_mock.delete(url, status_code=404)

    client.delete_company_by_ch_id(ch_id='')

    assert requests_mock.last_request.url == url


def test_delete_company_should_make_request_on_empty_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/'
    requests_mock.delete(url)

    client.delete_company_by_ch_id(ch_id='')

    assert requests_mock.last_request.url == url


def test_delete_company_should_make_request_on_no_ch_id(client, requests_mock):
    url = 'http://test.uk/testapi/company/None/'
    requests_mock.delete(url)

    client.delete_company_by_ch_id(ch_id=None)

    assert requests_mock.last_request.url == url


def test_delete_company(client, requests_mock):
    url = 'http://test.uk/testapi/company/12345678/'
    requests_mock.delete(url)

    client.delete_company_by_ch_id(ch_id='12345678')

    assert requests_mock.last_request.url == url


def test_get_published_companies_without_optional_parameters(client, requests_mock):
    url = 'http://test.uk/testapi/companies/published/'
    requests_mock.get(url)

    client.get_published_companies()

    assert requests_mock.last_request.url == url


def test_get_published_companies_check_request(client, requests_mock):
    url = 'http://test.uk/testapi/companies/published/'
    requests_mock.get(url)

    client.get_published_companies()

    assert requests_mock.last_request.url == url


def test_get_published_companies_with_both_filters(client, requests_mock):
    url = 'http://test.uk/testapi/companies/published/?limit=10&minimal_number_of_sectors=5'
    requests_mock.get(url)

    client.get_published_companies(limit=10, minimal_number_of_sectors=5)

    assert requests_mock.last_request.url.startswith(url)
    assert 'limit=10' in requests_mock.last_request.url
    assert 'minimal_number_of_sectors=5' in requests_mock.last_request.url


def test_get_published_companies_with_one_filter(client, requests_mock):
    url = 'http://test.uk/testapi/companies/published/?minimal_number_of_sectors=5'
    requests_mock.get(url)

    client.get_published_companies(minimal_number_of_sectors=5)

    assert requests_mock.last_request.url.startswith(url)
    assert 'minimal_number_of_sectors=5' in requests_mock.last_request.url


def test_get_company_by_ch_id_with_authenticator(client, requests_mock, basic_authenticator):
    url = 'http://test.uk/testapi/company/12345678/'
    requests_mock.get(url)
    client.get_company_by_ch_id(ch_id='12345678', authenticator=basic_authenticator)

    assert requests_mock.last_request.headers['Authorization'].startswith('Basic ')


def test_delete_company_by_ch_id_with_authenticator(client, requests_mock, basic_authenticator):
    url = 'http://test.uk/testapi/company/ch_ID_00/'
    requests_mock.delete(url)

    client.delete_company_by_ch_id(ch_id='ch_ID_00', authenticator=basic_authenticator)

    assert requests_mock.last_request.headers['Authorization'].startswith('Basic ')


def test_get_published_companies_without_optional_parameters_with_authenticator(
    client, requests_mock, basic_authenticator
):
    url = 'http://test.uk/testapi/companies/published/'
    requests_mock.get(url)

    client.get_published_companies(authenticator=basic_authenticator)

    assert requests_mock.last_request.headers['Authorization'].startswith('Basic ')

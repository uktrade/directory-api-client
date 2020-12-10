import pytest

from directory_api_client.buyer import BuyerAPIClient
from directory_api_client.client import DirectoryAPIClient
from directory_api_client.company import CompanyAPIClient
from directory_api_client.enrolment import EnrolmentAPIClient
from directory_api_client.exporting import ExportingAPIClient
from directory_api_client.personalisation import PersonalisationAPIClient
from directory_api_client.supplier import SupplierAPIClient


@pytest.fixture
def client():
    return DirectoryAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_exporting(client, requests_mock):
    assert isinstance(client.exporting, ExportingAPIClient)
    assert client.exporting.base_url == 'https://example.com'
    assert client.exporting.request_signer.secret == 'test'


def test_enrolment(client, requests_mock):
    assert isinstance(client.enrolment, EnrolmentAPIClient)
    assert client.enrolment.base_url == 'https://example.com'
    assert client.enrolment.request_signer.secret == 'test'


def test_company(client, requests_mock):
    assert isinstance(client.company, CompanyAPIClient)
    assert client.company.base_url == 'https://example.com'
    assert client.company.request_signer.secret == 'test'


def test_supplier(client, requests_mock):
    assert isinstance(client.supplier, SupplierAPIClient)
    assert client.supplier.base_url == 'https://example.com'
    assert client.supplier.request_signer.secret == 'test'


def test_buyer(client, requests_mock):
    assert isinstance(client.buyer, BuyerAPIClient)
    assert client.buyer.base_url == 'https://example.com'
    assert client.buyer.request_signer.secret == 'test'


def test_personalisation(client, requests_mock):
    assert isinstance(client.personalisation, PersonalisationAPIClient)
    assert client.personalisation.base_url == 'https://example.com'
    assert client.personalisation.request_signer.secret == 'test'


def test_ping(client, requests_mock):
    url = 'https://example.com/healthcheck/ping/'
    requests_mock.get(url)

    client.ping()

    assert requests_mock.last_request.url == url


def test_timeout(client):
    assert client.timeout == 5


def test_sender_id(client):
    assert client.request_signer.sender_id == 'test'

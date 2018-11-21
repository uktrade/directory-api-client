from unittest import TestCase

from directory_api_client.buyer import BuyerAPIClient
from directory_api_client.client import DirectoryAPIClient
from directory_api_client.company import CompanyAPIClient
from directory_api_client.enrolment import EnrolmentAPIClient
from directory_api_client.supplier import SupplierAPIClient
from directory_api_client.exporting import ExportingAPIClient

from directory_api_client.version import __version__

from tests import stub_request


class DirectoryAPIClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://example.com'
        self.key = 'test'
        self.client = DirectoryAPIClient(
            base_url='https://example.com',
            api_key='test',
            sender_id='test',
            timeout=5,
        )

    def test_exporting(self):
        assert isinstance(self.client.exporting, ExportingAPIClient)
        assert self.client.exporting.base_url == self.base_url
        assert (
            self.client.exporting.request_signer.secret == self.key
        )

    def test_enrolment(self):
        assert isinstance(self.client.enrolment, EnrolmentAPIClient)
        assert self.client.enrolment.base_url == self.base_url
        assert (
            self.client.enrolment.request_signer.secret == self.key
        )

    def test_company(self):
        assert isinstance(self.client.company, CompanyAPIClient)
        assert self.client.company.base_url == self.base_url
        assert self.client.company.request_signer.secret == self.key

    def test_supplier(self):
        assert isinstance(self.client.supplier, SupplierAPIClient)
        assert self.client.supplier.base_url == self.base_url
        assert self.client.supplier.request_signer.secret == self.key

    def test_buyer(self):
        assert isinstance(self.client.buyer, BuyerAPIClient)
        assert self.client.buyer.base_url == self.base_url
        assert self.client.buyer.request_signer.secret == self.key

    @stub_request('https://example.com/healthcheck/ping/', 'get')
    def test_ping(self, stub):
        self.client.ping()

        request = stub.request_history[0]
        assert request

    def test_timeout(self):
        assert self.client.timeout == 5

    def test_sender_id(self):
        assert self.client.request_signer.sender_id == 'test'

    def test_version(self):
        assert DirectoryAPIClient.version == __version__

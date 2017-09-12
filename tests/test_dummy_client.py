from unittest import TestCase
from unittest.mock import MagicMock

from directory_api_client.buyer import BuyerAPIClient
from directory_api_client.company import CompanyAPIClient
from directory_api_client.enrolment import EnrolmentAPIClient
from directory_api_client.exportopportunity import ExportOpportunityAPIClient
from directory_api_client.notifications import NotificationsAPIClient
from directory_api_client.supplier import SupplierAPIClient

from directory_api_client.dummy_client import DummyDirectoryAPIClient


class DirectoryAPIExternalClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://buyer.com'
        self.api_key = 'test'
        self.client = DummyDirectoryAPIClient(
            self.base_url, self.api_key
        )

    def test_buyer(self):
        assert isinstance(self.client.buyer, BuyerAPIClient)
        assert self.client.buyer.base_url == self.base_url
        assert self.client.buyer.request_signer.secret == self.api_key

    def test_company(self):
        company = self.client.company
        assert isinstance(company, CompanyAPIClient)
        assert company.base_url == self.base_url
        assert company.request_signer.secret == self.api_key

    def test_enrolment(self):
        enrolment = self.client.enrolment
        assert isinstance(enrolment, EnrolmentAPIClient)
        assert enrolment.base_url == self.base_url
        assert enrolment.request_signer.secret == self.api_key

    def test_exportopportunity(self):
        exportopportunity = self.client.exportopportunity
        assert isinstance(exportopportunity, ExportOpportunityAPIClient)
        assert exportopportunity.base_url == self.base_url
        assert exportopportunity.request_signer.secret == self.api_key

    def test_notifications(self):
        notifications = self.client.notifications
        assert isinstance(notifications, NotificationsAPIClient)
        assert notifications.base_url == self.base_url
        assert notifications.request_signer.secret == self.api_key

    def test_supplier(self):
        supplier = self.client.supplier
        assert isinstance(supplier, SupplierAPIClient)
        assert supplier.base_url == self.base_url
        assert supplier.request_signer.secret == self.api_key

    def test_buyer_send_mocked(self):
        response = self.client.buyer.send(method='get', url='http://1.com')

        assert isinstance(response.json(), MagicMock)

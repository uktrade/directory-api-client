from unittest import TestCase

from directory_api_client.buyer import BuyerAPIClient
from directory_api_client.client import DirectoryAPIClient
from directory_api_client.company import CompanyAPIClient
from directory_api_client.registration import EnrolmentAPIClient
from directory_api_client.user import UserAPIClient


class DirectoryAPIClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://example.com'
        self.api_key = 'test'
        self.client = DirectoryAPIClient(self.base_url, self.api_key)

    def test_registration(self):
        assert isinstance(self.client.registration, EnrolmentAPIClient)
        assert self.client.registration.base_url == self.base_url
        assert self.client.registration.api_key == self.api_key

    def test_company(self):
        assert isinstance(self.client.company, CompanyAPIClient)
        assert self.client.company.base_url == self.base_url
        assert self.client.company.api_key == self.api_key

    def test_user(self):
        assert isinstance(self.client.user, UserAPIClient)
        assert self.client.user.base_url == self.base_url
        assert self.client.user.api_key == self.api_key

    def test_buyer(self):
        assert isinstance(self.client.buyer, BuyerAPIClient)
        assert self.client.buyer.base_url == self.base_url
        assert self.client.user.api_key == self.api_key

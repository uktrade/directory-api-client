from unittest import TestCase

from tests import stub_request

from directory_api_client.supplier import SupplierAPIClient


class SupplierAPIClientTest(TestCase):

    def setUp(self):
        self.client = SupplierAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/supplier/1/', 'patch')
    def test_update_profile(self, stub):
        data = {'key': 'value'}
        self.client.update_profile(sso_id=1, data=data)
        request = stub.request_history[0]
        assert request.json() == data

    @stub_request('https://example.com/supplier/1/', 'get')
    def test_retrieve_profile(self, stub):
        self.client.retrieve_profile(sso_id=1)

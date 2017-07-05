from unittest import TestCase

from tests import stub_request

from directory_api_client.supplier import SupplierAPIClient


class SupplierAPIClientTest(TestCase):

    def setUp(self):
        self.client = SupplierAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/supplier/', 'patch')
    def test_update_profile(self, stub):
        data = {'key': 'value'}
        self.client.update_profile(sso_session_id=1, data=data)

        request = stub.request_history[0]
        assert request.json() == data
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://example.com/supplier/', 'get')
    def test_retrieve_profile(self, stub):
        self.client.retrieve_profile(sso_session_id=1)

    @stub_request('https://example.com/supplier/unsubscribe/', 'post')
    def test_unsubscribe(self, stub):
        self.client.unsubscribe(sso_session_id=1)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

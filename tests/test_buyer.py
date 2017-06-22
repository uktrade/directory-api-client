from unittest import TestCase

from tests import stub_request

from directory_api_client.buyer import BuyerAPIClient


class BuyerAPIClientTest(TestCase):

    def setUp(self):
        self.enrolment_client = BuyerAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/buyer/', 'post')
    def test_send_form(self, stub):
        form_data = {'field': 'value'}

        self.enrolment_client.send_form(form_data)

        request = stub.request_history[0]
        assert request.json() == form_data

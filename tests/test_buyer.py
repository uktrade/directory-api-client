from unittest import TestCase

from tests import stub_request

from directory_api_client.buyer import BuyerAPIClient


class BuyerAPIClientTest(TestCase):

    def setUp(self):
        self.enrolment_client = BuyerAPIClient(
            base_url='https://example.com',
            api_key='test',
            sender_id='test',
            timeout=5,
        )

    @stub_request('https://example.com/buyer/', 'post')
    def test_send_form(self, stub):
        form_data = {'field': 'value'}

        self.enrolment_client.send_form(form_data)

        request = stub.request_history[0]
        assert request.json() == form_data

    @stub_request('https://example.com/buyer/csv-dump/', 'get')
    def test_get_csv_dump(self, stub):
        token = 'debug'
        self.enrolment_client.get_csv_dump(token)
        request = stub.request_history[0]
        assert request.qs == {'token': ['debug']}

from unittest import TestCase

from tests import stub_request

from directory_api_client.exportopportunity import ExportOpportunityAPIClient


class ExportOpportunityAPIClientTestCase(TestCase):

    def setUp(self):
        self.client = ExportOpportunityAPIClient(
            base_url='https://e.com', api_key='test'
        )

    @stub_request('https://e.com/export-opportunity/food/', 'post')
    def test_create_opportunity_food(self, stub):
        form_data = {'field': 'value'}
        self.client.create_opportunity_food(form_data)

        request = stub.request_history[0]
        assert request.json() == form_data

    @stub_request('https://e.com/export-opportunity/legal/', 'post')
    def test_create_opportunity_legal(self, stub):
        form_data = {'field': 'value'}
        self.client.create_opportunity_legal(form_data)

        request = stub.request_history[0]
        assert request.json() == form_data

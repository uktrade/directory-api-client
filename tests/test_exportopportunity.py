from unittest import TestCase

from tests import stub_request

from directory_api_client.exportopportunity import ExportOpportunityAPIClient


class ExportOpportunityAPIClientTestCase(TestCase):

    def setUp(self):
        self.client = ExportOpportunityAPIClient(
            base_url='https://e.com', api_key='test'
        )

    @stub_request('https://e.com/export-opportunity/', 'post')
    def test_anonymous_unsubscribe(self, stub):
        form_data = {'field': 'value'}
        self.client.create_opportunity(form_data)

        request = stub.request_history[0]
        assert request.json() == form_data

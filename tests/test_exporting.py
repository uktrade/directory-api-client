from unittest import TestCase

from tests import stub_request

from directory_api_client.exporting import ExportingAPIClient


class ExportingAPIClientTest(TestCase):

    def setUp(self):
        self.client = ExportingAPIClient(
            base_url='https://example.com',
            api_key='test',
            sender_id='test',
            timeout=5,
        )

    @stub_request(
        'https://example.com/exporting/lookup-by-postcode/ABC%20123/', 'get'
    )
    def test_lookup_regional_office_by_postcode(self, stub):
        self.client.lookup_regional_office_by_postcode(
            postcode='ABC 123'
        )

    @stub_request(
        'https://example.com/exporting/lookup-by-postcode-get-all/ABC%20123/',
        'get'
    )
    def test_lookup_regional_office_by_postcode_get_all(self, stub):
        self.client.lookup_regional_office_by_postcode_get_all(
            postcode='ABC 123'
        )

from unittest import TestCase, mock

from directory_api_client.redirects import RedirectsAPIClient


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({"source_url": "foor"}, 200)


class RedirectsAPIClientTest(TestCase):

    def setUp(self):
        self.client = RedirectsAPIClient(
            base_url='https://example.com',
            api_key='test',
            sender_id='test',
            timeout=5,
        )

    @mock.patch.object(RedirectsAPIClient, 'lookup_redirect_by_url')
    def test_lookup_redirect_by_url(self, stub):
        self.client.lookup_redirect_by_url(source_url='foor')

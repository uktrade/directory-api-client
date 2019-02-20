from unittest import mock, TestCase

from directory_api_client.base import AbstractAPIClient


class APIClient(AbstractAPIClient):

    version = 123


class AbstractAPIClientTest(TestCase):

    def setUp(self):
        self.client = APIClient(
            base_url='https://example.com',
            api_key='test',
            sender_id='test',
            timeout=5,
        )

    @mock.patch.object(AbstractAPIClient, 'fallback_cache_get')
    def test_fallback_cache_used(self, mock_fallback_cache_get):
        self.client.get('http://www.thing.com', use_fallback_cache=True)

        assert mock_fallback_cache_get.call_count == 1
        assert mock_fallback_cache_get.call_args == mock.call(
            'http://www.thing.com'
        )

    @mock.patch.object(AbstractAPIClient, 'get')
    @mock.patch.object(AbstractAPIClient, 'fallback_cache_get')
    def test_fallback_cache_not_used(self, mock_fallback_cache_get, mock_get):
        self.client.get('http://www.thing.com')

        assert mock_fallback_cache_get.call_count == 0
        assert mock_get.call_count == 1

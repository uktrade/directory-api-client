from directory_api_client.base import AbstractAPIClient
from django.core.cache import caches

from directory_client_core.helpers import ttl


class RedirectsAPIClient(AbstractAPIClient):

    endpoints = {
        'lookup-by-url': '/redirects/urls/{source_url}/',
    }

    @ttl(cache=caches['redirect'], seconds=1800)
    def lookup_redirect_by_url(self, source_url):
        response = self.get(
            url=self.endpoints['lookup-by-url'].format(source_url=source_url),
            use_fallback_cache=False,
        )
        return response.json()

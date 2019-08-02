from directory_api_client.base import AbstractAPIClient
from directory_api_client.version import __version__
from django.http import HttpResponseNotFound


class RedirectsAPIClient(AbstractAPIClient):

    endpoints = {
        'lookup-by-url': '/redirects/urls/{source_url}/',
    }
    version = __version__

    def lookup_redirect_by_url(self, source_url):
        response = self.get(
            url=self.endpoints['lookup-by-url'].format(source_url=source_url),
            use_fallback_cache=False,
        )
        return response.json()

from directory_client_core.base import AbstractAPIClient
from directory_client_core.helpers import fallback

from django.core.cache import caches

from directory_api_client.version import __version__


class ExportingAPIClient(AbstractAPIClient):

    endpoints = {
        'lookup-by-postcode': '/exporting/lookup-by-postcode/{postcode}/',
    }
    version = __version__

    @fallback(cache=caches['api_fallback'])
    def lookup_regional_office_by_postcode(self, postcode):
        url = self.endpoints['lookup-by-postcode'].format(postcode=postcode)
        return self.get(url)

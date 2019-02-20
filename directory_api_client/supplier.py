from directory_client_core.authentication import SessionSSOAuthenticator
from directory_client_core.base import AbstractAPIClient
from directory_client_core.helpers import fallback

from django.core.cache import caches

from directory_api_client.version import __version__


class SupplierAPIClient(AbstractAPIClient):

    endpoints = {
        'supplier': '/supplier/',
        'unsubscribe': '/supplier/unsubscribe/',
        'csv-dump': 'supplier/csv-dump/'
    }
    authenticator = SessionSSOAuthenticator
    version = __version__

    def update_profile(self, sso_session_id, data):
        return self.patch(
            self.endpoints['supplier'],
            data=data,
            authenticator=self.authenticator(sso_session_id)
        )

    @fallback(cache=caches['api_fallback'])
    def retrieve_profile(self, sso_session_id):
        url = self.endpoints['supplier']
        return self.get(url, authenticator=self.authenticator(sso_session_id))

    def unsubscribe(self, sso_session_id):
        url = self.endpoints['unsubscribe']
        return self.post(url, authenticator=self.authenticator(sso_session_id))

    def get_csv_dump(self, token):
        url = self.endpoints['csv-dump']
        return self.get(url,  params={'token': token})

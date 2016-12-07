from directory_api_client.base import BaseAPIClient


class SupplierAPIClient(BaseAPIClient):

    endpoints = {
        'supplier': '/supplier/{sso_id}/',
    }

    def update_profile(self, sso_id, data):
        url = self.endpoints['supplier'].format(sso_id=sso_id)
        return self.patch(url, data=data)

    def retrieve_profile(self, sso_id):
        url = self.endpoints['supplier'].format(sso_id=sso_id)
        return self.get(url)

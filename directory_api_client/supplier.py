from directory_api_client.base import BaseAPIClient


class SupplierAPIClient(BaseAPIClient):

    endpoints = {
        'supplier': '/supplier/',
        'unsubscribe': '/supplier/unsubscribe/',
    }

    def update_profile(self, sso_session_id, data):
        url = self.endpoints['supplier']
        return self.patch(url, data=data, sso_session_id=sso_session_id)

    def retrieve_profile(self, sso_session_id):
        url = self.endpoints['supplier']
        return self.get(url, sso_session_id=sso_session_id)

    def unsubscribe(self, sso_session_id):
        url = self.endpoints['unsubscribe']
        return self.post(url, sso_session_id=sso_session_id)

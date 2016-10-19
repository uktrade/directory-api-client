from directory_api_client.base import BaseAPIClient


class UserAPIClient(BaseAPIClient):

    endpoints = {
        'user': '/user/{id}/'
    }

    def update_profile(self, id, data):
        url = self.endpoints['user'].format(id=id)
        return self.patch(url, data=data)

    def retrieve_profile(self, id):
        url = '/user/{id}/'.format(id=id)
        return self.get(url)

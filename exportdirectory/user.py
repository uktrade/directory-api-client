from exportdirectory.base import BaseAPIClient


class UserAPIClient(BaseAPIClient):

    def update_profile(self, id, data):
        return self.patch(
            '/user/{id}/'.format(id=id),
            data=data
        )

    def retrieve_profile(self, id):
        return self.get('/user/{id}/'.format(id=id))

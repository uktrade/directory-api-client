from exportdirectory.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    def update_profile(self, id, data):
        return self.patch(
            '/company/{id}/'.format(id=id),
            data=data
        )

    def retrieve_profile(self, id):
        return self.get('/company/{id}/'.format(id=id))

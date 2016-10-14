from exportdirectory.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    def update_profile(self, id, data):
        files = {}
        if 'logo' in data:
            files['logo'] = data.pop('logo')
        return self.patch(
            '/company/{id}/'.format(id=id),
            data=data,
            files=files,
        )

    def retrieve_profile(self, id):
        return self.get('/company/{id}/'.format(id=id))

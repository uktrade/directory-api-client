from exportdirectory.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    endpoints = {
        'profile': '/company/{id}/',
    }

    def update_profile(self, id, data):
        files = {}
        if 'logo' in data:
            files['logo'] = data.pop('logo')
        url = self.endpoints['profile'].format(id=id)
        return self.patch(
            url=url,
            data=data,
            files=files,
        )

    def retrieve_profile(self, id):
        url = self.endpoints['profile'].format(id=id)
        return self.get(url)

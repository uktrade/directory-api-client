from directory_api_client.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    endpoints = {
        'profile': '/company/{id}/',
        'validate-company-number': '/validate-company-number/',
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

    def validate_company_number(self, number):
        url = self.endpoints['validate-company-number']
        params = {'number': number}
        return self.get(url, params=params)

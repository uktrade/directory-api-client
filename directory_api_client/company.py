from directory_api_client.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    endpoints = {
        'profile': '/company/details/{id}/',
        'validate-company-number': '/validate-company-number/',
        'companies-house-profile': '/company/companies-house-profile/',
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

    def retrieve_companies_house_profile(self, number):
        url = self.endpoints['companies-house-profile']
        return self.get(url, {'number': number})

    def validate_company_number(self, number):
        url = self.endpoints['validate-company-number']
        params = {'number': number}
        return self.get(url, params=params)

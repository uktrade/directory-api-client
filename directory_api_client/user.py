from directory_api_client.base import BaseAPIClient


class UserAPIClient(BaseAPIClient):

    endpoints = {
        'user': '/user/{sso_id}/',
        'validate-email-address': '/validate-email-address/',
    }

    def update_profile(self, sso_id, data):
        url = self.endpoints['user'].format(sso_id=sso_id)
        return self.patch(url, data=data)

    def retrieve_profile(self, sso_id):
        url = '/user/{sso_id}/'.format(sso_id=sso_id)
        return self.get(url)

    def validate_email_address(self, email):
        url = self.endpoints['validate-email-address']
        params = {'company_email': email}
        return self.get(url, params=params)

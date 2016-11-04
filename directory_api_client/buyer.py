from directory_api_client.base import BaseAPIClient


class BuyerAPIClient(BaseAPIClient):

    endpoints = {
        'save': 'buyer/',
    }

    def send_form(self, form_data):
        return self.post(
            self.endpoints['save'],
            data=form_data
        )

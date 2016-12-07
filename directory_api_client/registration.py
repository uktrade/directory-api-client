from directory_api_client.base import BaseAPIClient


class EnrolmentAPIClient(BaseAPIClient):

    endpoints = {
        'enrolment': '/enrolment/',
    }

    def send_form(self, form_data):
        return self.post(
            self.endpoints['enrolment'],
            data=form_data
        )

from exportdirectory.base import BaseAPIClient


class RegistrationAPIClient(BaseAPIClient):

    endpoints = {
        'enrolment': '/enrolment/',
        'confirm': '/enrolment/confirm/',
    }

    def send_form(self, form_data):
        return self.post(
            self.endpoints['enrolment'],
            data=form_data
        )

    def confirm_email(self, confirmation_code):
        return self.post(
            self.endpoints['confirm'],
            data=confirmation_code
        )

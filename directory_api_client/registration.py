from directory_api_client.base import BaseAPIClient


class EnrolmentAPIClient(BaseAPIClient):

    endpoints = {
        'confirm': '/enrolment/confirm/',
        'enrolment': '/enrolment/',
        'verification_sms': '/enrolment/verification-sms/',
    }

    def send_form(self, form_data):
        return self.post(
            self.endpoints['enrolment'],
            data=form_data
        )

    def confirm_email(self, confirmation_code):
        return self.post(
            self.endpoints['confirm'],
            data={'confirmation_code': confirmation_code}
        )

    def send_verification_sms(self, phone_number):
        return self.post(
            self.endpoints['verification_sms'],
            data={'phone_number': phone_number}
        )

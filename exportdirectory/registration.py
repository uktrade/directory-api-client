from exportdirectory.base import BaseAPIClient


class RegistrationAPIClient(BaseAPIClient):

    def send_form(self, form_data):
        return self.post(
            '/registration/',
            data=form_data
        )

    def confirm_email(self, confirmation_code):
        return self.post(
            '/registration/confirm',
            data=confirmation_code
        )

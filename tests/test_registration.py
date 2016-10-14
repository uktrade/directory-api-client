from unittest import TestCase

from tests import stub_request

from exportdirectory.registration import RegistrationAPIClient


class RegistrationAPIClientTest(TestCase):

    def setUp(self):
        self.registration_client = RegistrationAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/enrolment/', 'post')
    def test_send_form(self, stub):
        self.registration_client.send_form(
            form_data='form_data'
        )

    @stub_request('https://example.com/enrolment/confirm/', 'post')
    def test_confirm_email(self, stub):
        self.registration_client.confirm_email(
            confirmation_code='confirmation_code'
        )

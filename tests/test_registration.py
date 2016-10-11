from unittest import TestCase

from exportdirectory.registration import RegistrationAPIClient
from tests import mock_requests


class RegistrationAPIClientTest(TestCase):

    def setUp(self):
        self.registration_client = RegistrationAPIClient(
            base_url='https://example.com', api_key='test'
        )

    def test_send_form(self):
        with mock_requests():
            self.registration_client.send_form(
                form_data='form_data'
            )

    def test_confirm_email(self):
        with mock_requests():
            self.registration_client.confirm_email(
                confirmation_code='confirmation_code'
            )

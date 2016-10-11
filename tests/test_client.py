from unittest import TestCase

from exportdirectory.client import DirectoryAPIClient
from tests import mock_requests


class DirectoryAPIClientTest(TestCase):

    def setUp(self):
        self.directory_client = DirectoryAPIClient(
            base_url='https://example.com', api_key='test'
        )

    def test_registration_send_form(self):
        with mock_requests():
            self.directory_client.registration.send_form(
                form_data='form_data'
            )

    def test_confirm_email(self):
        with mock_requests():
            self.directory_client.registration.confirm_email(
                confirmation_code='confirmation_code'
            )

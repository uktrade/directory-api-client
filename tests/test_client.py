from unittest import TestCase

from tests import stub_request

from exportdirectory.client import DirectoryAPIClient


class DirectoryAPIClientTest(TestCase):

    def setUp(self):
        self.directory_client = DirectoryAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/enrolment/', 'post')
    def test_registration_send_form(self):
        self.directory_client.registration.send_form(
            form_data='form_data'
        )

    @stub_request('https://example.com/enrolment/confirm/', 'post')
    def test_confirm_email(self):
        self.directory_client.registration.confirm_email(
            confirmation_code='confirmation_code'
        )

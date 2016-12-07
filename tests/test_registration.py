from unittest import TestCase

from tests import stub_request

from directory_api_client.registration import EnrolmentAPIClient


class EnrolmentAPIClientTest(TestCase):

    def setUp(self):
        self.registration_client = EnrolmentAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/enrolment/', 'post')
    def test_send_form(self, stub):
        self.registration_client.send_form(
            form_data='form_data'
        )

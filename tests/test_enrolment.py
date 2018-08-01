from unittest import TestCase

from tests import stub_request

from directory_api_client.enrolment import EnrolmentAPIClient


class EnrolmentAPIClientTest(TestCase):

    def setUp(self):
        self.enrolment_client = EnrolmentAPIClient(
            base_url='https://example.com',
            api_key='test',
            sender_id='test',
            timeout=5,
        )

    @stub_request('https://example.com/enrolment/', 'post')
    def test_send_form(self, stub):
        self.enrolment_client.send_form(
            form_data='form_data'
        )

    @stub_request('https://example.com/trusted-code/2/', 'get')
    def test_retrieve_trusted_source_signup_details(self, stub):
        self.enrolment_client.retrieve_trusted_source_signup_details(code=2)

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

    @stub_request('https://example.com/enrolment/claim-preverified/', 'post')
    def test_claim_prepeveried_company(self, stub):
        data = {
            'key': '123',
            'name': 'Foo Bar'
        }
        self.enrolment_client.claim_prepeveried_company(
            sso_session_id='2',
            data=data
        )

        request = stub.request_history[0]
        assert request.json() == data
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 2'

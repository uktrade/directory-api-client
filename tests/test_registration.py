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

    @stub_request('https://example.com/enrolment/confirm/', 'post')
    def test_confirm_email(self, stub):
        self.registration_client.confirm_email(
            confirmation_code='123'
        )
        request = stub.request_history[0]
        assert request.json() == {'confirmation_code': '123'}

    @stub_request('https://example.com/enrolment/verification-sms/', 'post')
    def test_send_verification_sms(self, stub):
        self.registration_client.send_verification_sms(
            phone_number='333'
        )
        request = stub.request_history[0]
        assert request.json() == {'phone_number': '333'}

from unittest import TestCase

from tests import stub_request

from directory_api_client.exportreadiness import ExportReadinessAPIClient


class ExportReadinessAPIClientTestCase(TestCase):

    def setUp(self):
        self.client = ExportReadinessAPIClient(
            base_url='https://e.com', api_key='test'
        )

    @stub_request('https://e.com/export-readiness/triage/', 'get')
    def test_retrieve_triage_resukt(self, stub):
        self.client.retrieve_triage_result(sso_session_id=1)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://e.com/export-readiness/triage/', 'post')
    def test_create_triage_result(self, stub):
        form_data = {'field': 'value'}
        self.client.create_triage_result(form_data, sso_session_id=1)

        request = stub.request_history[0]
        assert request.json() == form_data
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

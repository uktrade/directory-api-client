from unittest import TestCase

from tests import stub_request

from directory_api_client.exportreadiness import ExportReadinessAPIClient


class ExportReadinessAPIClientTestCase(TestCase):

    def setUp(self):
        self.client = ExportReadinessAPIClient(
            base_url='https://e.com', api_key='test'
        )

    @stub_request('https://e.com/export-readiness/triage/', 'get')
    def test_retrieve_triage_result(self, stub):
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

    @stub_request('https://e.com/export-readiness/triage/', 'patch')
    def test_update_triage_result(self, stub):
        form_data = {'field': 'value'}
        self.client.update_triage_result(form_data, sso_session_id=1)

        request = stub.request_history[0]
        assert request.json() == form_data
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://e.com/export-readiness/article-read/', 'get')
    def test_retrieve_article_read(self, stub):
        self.client.retrieve_article_read(sso_session_id=1)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://e.com/export-readiness/article-read/', 'post')
    def test_create_article_read(self, stub):
        article_uuid = '123'
        self.client.create_article_read(article_uuid, sso_session_id=1)

        request = stub.request_history[0]
        assert request.json() == {'article_uuid': article_uuid}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://e.com/export-readiness/article-read/', 'post')
    def test_bulk_create_article_read(self, stub):
        self.client.bulk_create_article_read(['1', '2'], sso_session_id=1)

        request = stub.request_history[0]
        assert request.json() == [{'article_uuid': '1'}, {'article_uuid': '2'}]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://e.com/export-readiness/task-completed/', 'get')
    def test_retrieve_task_completed(self, stub):
        self.client.retrieve_task_completed(sso_session_id=1)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('https://e.com/export-readiness/task-completed/', 'post')
    def test_create_task_completed(self, stub):
        task_uuid = '123'
        self.client.create_task_completed(task_uuid, sso_session_id=1)

        request = stub.request_history[0]
        assert request.json() == {'task_uuid': task_uuid}
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

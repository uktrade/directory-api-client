from directory_api_client.base import BaseAPIClient


class ExportReadinessAPIClient(BaseAPIClient):

    endpoints = {
        'triage-result': 'export-readiness/triage/',
        'create-retrieve-article-read': 'export-readiness/article-read/',
        'create-retrieve-task-completed': 'export-readiness/task-completed/'
    }

    def retrieve_triage_result(self, sso_session_id):
        return self.get(
            self.endpoints['triage-result'],
            sso_session_id=sso_session_id
        )

    def create_triage_result(self, form_data, sso_session_id):
        return self.post(
            self.endpoints['triage-result'],
            data=form_data,
            sso_session_id=sso_session_id
        )

    def update_triage_result(self, form_data, sso_session_id):
        return self.patch(
            self.endpoints['triage-result'],
            data=form_data,
            sso_session_id=sso_session_id
        )

    def retrieve_article_read(self, sso_session_id):
        return self.get(
            self.endpoints['create-retrieve-article-read'],
            sso_session_id=sso_session_id
        )

    def create_article_read(self, article_uuid, sso_session_id):
        return self.post(
            self.endpoints['create-retrieve-article-read'],
            data={'article_uuid': article_uuid},
            sso_session_id=sso_session_id
        )

    def retrieve_task_completed(self, sso_session_id):
        return self.get(
            self.endpoints['create-retrieve-task-completed'],
            sso_session_id=sso_session_id
        )

    def create_task_completed(self, task_uuid, sso_session_id):
        return self.post(
            self.endpoints['create-retrieve-task-completed'],
            data={'task_uuid': task_uuid},
            sso_session_id=sso_session_id
        )

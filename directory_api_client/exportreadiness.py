from directory_api_client.base import BaseAPIClient


class ExportReadinessAPIClient(BaseAPIClient):

    endpoints = {
        'create-retrieve-triage-result': 'export-readiness/triage/',
        'create-retrieve-article-read': 'export-readiness/article-read/',
        'create-retrieve-task-completed': 'export-readiness/task-completed/'
    }

    def retrieve_triage_result(self, sso_session_id):
        return self.get(
            self.endpoints['create-retrieve-triage-result'],
            sso_session_id=sso_session_id
        )

    def create_triage_result(self, form_data, sso_session_id):
        return self.post(
            self.endpoints['create-retrieve-triage-result'],
            data=form_data,
            sso_session_id=sso_session_id
        )

    def retrieve_article_read(self, sso_session_id):
        return self.get(
            self.endpoints['create-retrieve-article-read'],
            sso_session_id=sso_session_id
        )

    def create_article_read(self, form_data, sso_session_id):
        return self.post(
            self.endpoints['create-retrieve-article-read'],
            data=form_data,
            sso_session_id=sso_session_id
        )

    def retrieve_task_completed(self, sso_session_id):
        return self.get(
            self.endpoints['create-retrieve-task-completed'],
            sso_session_id=sso_session_id
        )

    def create_task_completed(self, form_data, sso_session_id):
        return self.post(
            self.endpoints['create-retrieve-task-completed'],
            data=form_data,
            sso_session_id=sso_session_id
        )

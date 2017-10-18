from directory_api_client.base import BaseAPIClient


class ExportReadinessAPIClient(BaseAPIClient):

    endpoints = {
        'create-retrieve-triage-result': 'export-readiness/triage/',
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

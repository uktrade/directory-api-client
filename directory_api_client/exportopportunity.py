from directory_api_client.base import BaseAPIClient


class ExportOpportunityAPIClient(BaseAPIClient):

    endpoints = {
        'create-opportunity': '/export-opportunity/',
    }

    def create_opportunity(self, form_data):
        return self.post(
            self.endpoints['create-opportunity'],
            data=form_data
        )

from directory_api_client.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    endpoints = {
        'profile': '/user/{sso_id}/company/',
        'validate-company-number': '/validate/company-number/',
        'case-study-detail': '/company/case-study/{id}/',
        'case-study-list': '/company/case-study/',
    }

    def update_profile(self, sso_user_id, data):
        files = {}
        if 'logo' in data:
            files['logo'] = data.pop('logo')
        url = self.endpoints['profile'].format(sso_id=sso_user_id)
        return self.patch(
            url=url,
            data=data,
            files=files,
        )

    def retrieve_profile(self, sso_user_id):
        url = self.endpoints['profile'].format(sso_id=sso_user_id)
        return self.get(url)

    def validate_company_number(self, number):
        url = self.endpoints['validate-company-number']
        params = {'number': number}
        return self.get(url, params=params)

    def create_supplier_case_study(self, data):
        url = self.endpoints['case-study-list']
        return self.post(url, data=data)

    def update_supplier_case_study(self, data, case_study_id):
        url = self.endpoints['case-study-detail'].format(id=case_study_id)
        return self.patch(url, data=data)

    def delete_supplier_case_study(self, case_study_id):
        url = self.endpoints['case-study-detail'].format(id=case_study_id)
        return self.delete(url)

from directory_api_client.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    endpoints = {
        'profile': '/user/{sso_id}/company/',
        'case-study-detail': '/user/{sso_id}/company/case-study/{id}/',
        'case-study-list': '/user/{sso_id}/company/case-study/',
        'validate-company-number': '/validate/company-number/',
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

    def create_supplier_case_study(self, data, sso_user_id):
        files = {}
        for field in ['image_one', 'image_two', 'image_three', 'video_one']:
            if data.get(field):
                files[field] = data.pop(field)
        url = self.endpoints['case-study-list'].format(sso_id=sso_user_id)
        return self.post(url, data=data, files=files)

    def update_supplier_case_study(self, data, sso_user_id, case_study_id):
        files = {}
        for field in ['image_one', 'image_two', 'image_three', 'video_one']:
            if data.get(field):
                files[field] = data.pop(field)
        url = self.endpoints['case-study-detail'].format(
            sso_id=sso_user_id, id=case_study_id
        )
        return self.patch(url, data=data, files=files)

    def delete_supplier_case_study(self, sso_user_id, case_study_id):
        url = self.endpoints['case-study-detail'].format(
            id=case_study_id,
            sso_id=sso_user_id,
        )
        return self.delete(url)

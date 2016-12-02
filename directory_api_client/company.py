from urllib import parse

from directory_api_client.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    endpoints = {
        'profile': '/supplier/{sso_id}/company/',
        'case-study-detail': '/supplier/{sso_id}/company/case-study/{id}/',
        'case-study-list': '/supplier/{sso_id}/company/case-study/',
        'validate-company-number': '/validate/company-number/',
        'public-profile-detail': '/company/public/{number}/',
        'public-profile-list': '/company/public/',
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

    def retrieve_public_profile_by_companies_house_number(self, number):
        url = self.endpoints['public-profile-detail'].format(number=number)
        return self.get(url)

    def list_public_profiles(self, **kwargs):
        url = '{path}?{querystring}'.format(
            path=self.endpoints['public-profile-list'],
            querystring=parse.urlencode(kwargs),
        )
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

    def retrieve_supplier_case_study(self, sso_user_id, case_study_id):
        url = self.endpoints['case-study-detail'].format(
            sso_id=sso_user_id, id=case_study_id
        )
        return self.get(url)

    def delete_supplier_case_study(self, sso_user_id, case_study_id):
        url = self.endpoints['case-study-detail'].format(
            id=case_study_id,
            sso_id=sso_user_id,
        )
        return self.delete(url)

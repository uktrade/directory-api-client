from urllib import parse

from directory_api_client.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    endpoints = {
        'profile': '/supplier/{sso_id}/company/',
        'case-study-detail': '/supplier/{sso_id}/company/case-study/{id}/',
        'case-study-list': '/supplier/{sso_id}/company/case-study/',
        'validate-company-number': '/validate/company-number/',
        'verify': '/supplier/{sso_id}/company/verify/',
        'public-case-study-detail': '/public/case-study/{id}/',
        'public-profile-detail': '/public/company/{number}/',
        'public-profile-list': '/public/company/',
        'contact-supplier': '/contact/supplier/',
        'search': '/company/search/',
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

    def retrieve_private_profile(self, sso_user_id):
        url = self.endpoints['profile'].format(sso_id=sso_user_id)
        return self.get(url)

    def retrieve_public_profile(self, number):
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

    def create_case_study(self, data, sso_user_id):
        files = {}
        for field in ['image_one', 'image_two', 'image_three', 'video_one']:
            if data.get(field):
                files[field] = data.pop(field)
        url = self.endpoints['case-study-list'].format(sso_id=sso_user_id)
        return self.post(url, data=data, files=files)

    def update_case_study(self, data, sso_user_id, case_study_id):
        files = {}
        for field in ['image_one', 'image_two', 'image_three', 'video_one']:
            if data.get(field):
                files[field] = data.pop(field)
        url = self.endpoints['case-study-detail'].format(
            sso_id=sso_user_id, id=case_study_id
        )
        return self.patch(url, data=data, files=files)

    def retrieve_private_case_study(self, sso_user_id, case_study_id):
        url = self.endpoints['case-study-detail'].format(
            sso_id=sso_user_id, id=case_study_id
        )
        return self.get(url)

    def retrieve_public_case_study(self, case_study_id):
        url = self.endpoints['public-case-study-detail'].format(
            id=case_study_id
        )
        return self.get(url)

    def delete_case_study(self, sso_user_id, case_study_id):
        url = self.endpoints['case-study-detail'].format(
            id=case_study_id,
            sso_id=sso_user_id,
        )
        return self.delete(url)

    def verify_with_code(self, sso_user_id, code):
        url = self.endpoints['verify'].format(sso_id=sso_user_id)
        data = {'code': code}
        return self.post(url, data)

    def send_email(self, data):
        return self.post(self.endpoints['contact-supplier'], data)

    def search(self, term, page, size):
        params = {'term': term, 'page': page, 'size': size}
        return self.get(self.endpoints['search'], params=params)

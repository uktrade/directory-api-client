from urllib import parse

from directory_api_client.base import BaseAPIClient


class CompanyAPIClient(BaseAPIClient):

    endpoints = {
        'profile': '/supplier/company/',
        'case-study-detail': '/supplier/company/case-study/{id}/',
        'case-study-list': '/supplier/company/case-study/',
        'validate-company-number': '/validate/company-number/',
        'verify': '/supplier/company/verify/',
        'verify-companies-house': '/supplier/company/verify-companies-house/',
        'public-case-study-detail': '/public/case-study/{id}/',
        'public-profile-detail': '/public/company/{number}/',
        'public-profile-list': '/public/company/',
        'contact-supplier': '/contact/supplier/',
        'search': '/company/search/',
    }

    def update_profile(self, sso_session_id, data):
        files = {}
        if 'logo' in data:
            files['logo'] = data.pop('logo')
        return self.patch(
            url=self.endpoints['profile'],
            data=data,
            files=files,
            sso_session_id=sso_session_id,
        )

    def retrieve_private_profile(self, sso_session_id):
        url = self.endpoints['profile']
        return self.get(url, sso_session_id=sso_session_id)

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

    def create_case_study(self, data, sso_session_id):
        files = {}
        for field in ['image_one', 'image_two', 'image_three', 'video_one']:
            if data.get(field):
                files[field] = data.pop(field)
        url = self.endpoints['case-study-list']
        return self.post(
            url, data=data, files=files, sso_session_id=sso_session_id
        )

    def update_case_study(self, data, sso_session_id, case_study_id):
        files = {}
        for field in ['image_one', 'image_two', 'image_three', 'video_one']:
            if data.get(field):
                files[field] = data.pop(field)
        url = self.endpoints['case-study-detail'].format(id=case_study_id)
        return self.patch(
            url, data=data, files=files, sso_session_id=sso_session_id
        )

    def retrieve_private_case_study(self, sso_session_id, case_study_id):
        url = self.endpoints['case-study-detail'].format(id=case_study_id)
        return self.get(url, sso_session_id=sso_session_id)

    def retrieve_public_case_study(self, case_study_id):
        url = self.endpoints['public-case-study-detail'].format(
            id=case_study_id
        )
        return self.get(url)

    def delete_case_study(self, sso_session_id, case_study_id):
        url = self.endpoints['case-study-detail'].format(id=case_study_id)
        return self.delete(url, sso_session_id=sso_session_id)

    def verify_with_code(self, sso_session_id, code):
        data = {'code': code}
        return self.post(
            self.endpoints['verify'], data, sso_session_id=sso_session_id
        )

    def verify_with_companies_house(self, sso_session_id, access_token):
        data = {'access_token': access_token}
        url = self.endpoints['verify-companies-house']
        return self.post(url, data, sso_session_id=sso_session_id)

    def send_email(self, data):
        return self.post(self.endpoints['contact-supplier'], data)

    def search(self, term, page, size, sectors=None):
        params = {'term': term, 'page': page, 'size': size, 'sectors': sectors}
        return self.get(self.endpoints['search'], params=params)

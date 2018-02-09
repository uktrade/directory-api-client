from directory_api_client.base import BaseAPIClient


class DirectoryTestAPIClient(BaseAPIClient):

    endpoints = {
        'company_by_ch_id': 'testapi/company/{ch_id}/'
    }

    def get_company_by_ch_id(self, ch_id: str):
        result = None
        if ch_id:
            url = self.endpoints['company_by_ch_id'].format(ch_id=ch_id)
            result = self.get(url=url)
        return result

from directory_api_client.base import BaseAPIClient


class DirectoryTestAPIClient(BaseAPIClient):

    endpoints = {
        'company_by_ch_id': 'testapi/company/{ch_id}/'
    }

    def _get_url(self, ch_id):
        return self.endpoints['company_by_ch_id'].format(ch_id=ch_id)

    def get_company_by_ch_id(self, ch_id):
        url = self._get_url(ch_id)
        return self.get(url=url)

    def delete_company_by_ch_id(self, ch_id):
        url = self._get_url(ch_id)
        return self.delete(url=url)

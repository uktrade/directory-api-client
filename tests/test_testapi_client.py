from unittest import TestCase, mock

from tests import stub_request

from directory_api_client.testapiclient import DirectoryTestAPIClient


class DirectoryTestAPIClientTest(TestCase):

    url = 'https://example.com/testapi/company/'

    def setUp(self):
        self.base_url = 'https://example.com'
        self.key = 'test'
        self.client = DirectoryTestAPIClient(self.base_url, self.key)

    def test_company(self):
        assert isinstance(self.client, DirectoryTestAPIClient)
        assert self.client.base_url == self.base_url
        assert self.client.request_signer.secret == self.key

    def test_endpoints_urljoin(self):
        """urljoin replaces base_url's path if endpoints start with with / """
        for endpoint in self.client.endpoints.values():
            assert not endpoint.startswith('/')

    @stub_request(url + '12345678/', 'get')
    def test_get_company_by_ch_id(self, stub):
        ch_id = '12345678'
        response = self.client.get_company_by_ch_id(ch_id=ch_id)
        request = stub.request_history[0]
        assert request.url == response.url

    def test_get_company_should_return_404_on_missing_ch_id(self):
        response = self.client.get_company_by_ch_id(ch_id=None)
        assert response.status_code == 404

    def test_get_company_should_return_404_on_empty_ch_id(self):
        response = self.client.get_company_by_ch_id(ch_id='')
        assert response.status_code == 404

    @mock.patch('directory_api_client.base.BaseAPIClient.request')
    def test_get_company_should_make_request_on_empty_ch_id(
            self, mocked_request):
        self.client.get_company_by_ch_id(ch_id='')
        assert mocked_request.call_count == 1

    @mock.patch('directory_api_client.base.BaseAPIClient.request')
    def test_get_company(self, mocked_request):
        ch_id = '12345678'
        self.client.get_company_by_ch_id(ch_id=ch_id)

        assert mocked_request.call_count == 1
        assert mocked_request.call_args == mock.call(
            method='GET', params=None,
            url='testapi/company/{}/'.format(ch_id), sso_session_id=None
        )

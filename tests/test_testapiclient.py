from unittest import mock, TestCase

from hypothesis import given
from hypothesis import settings as hypothesis_settings
from hypothesis.strategies import text

from tests import stub_request

from directory_api_client.testapiclient import DirectoryTestAPIClient


class DirectoryTestAPIClientTest(TestCase):

    url = 'https://example.com/testapi/company/'

    def setUp(self):
        self.base_url = 'https://example.com'
        self.key = 'test'
        self.client = DirectoryTestAPIClient(self.base_url, self.key)

    def test_client_setup(self):
        assert isinstance(self.client, DirectoryTestAPIClient)
        assert self.client.base_url == self.base_url
        assert self.client.request_signer.secret == self.key

    def test_client_endpoints_urljoin(self):
        """urljoin replaces base_url's path if endpoints start with with / """
        for endpoint in self.client.endpoints.values():
            assert not endpoint.startswith('/')

    @stub_request(url + '12345678/', 'get')
    def test_get_company_by_ch_id(self, stub):
        ch_id = '12345678'
        response = self.client.get_company_by_ch_id(ch_id=ch_id)
        request = stub.request_history[0]
        assert request.url == response.url

    def test_should_return_none_on_missing_ch_id(self):
        response = self.client.get_company_by_ch_id(ch_id=None)
        assert response is None

    def test_should_return_none_on_empty_ch_id(self):
        response = self.client.get_company_by_ch_id(ch_id='')
        assert response is None

    @mock.patch('directory_api_client.base.BaseAPIClient.request')
    def test_should_not_make_any_request_on_empty_ch_id(self, mocked_request):
        self.client.get_company_by_ch_id(ch_id='')
        assert mocked_request.call_count == 0

    @mock.patch('directory_api_client.base.BaseAPIClient.request')
    def test_should_not_make_any_request_on_no_ch_id(self, mocked_request):
        self.client.get_company_by_ch_id(ch_id=None)
        assert mocked_request.call_count == 0

    @mock.patch('directory_api_client.base.BaseAPIClient.request')
    def test_get_company(self, mocked_request):
        ch_id = '12345678'
        self.client.get_company_by_ch_id(ch_id=ch_id)

        assert mocked_request.call_count == 1
        assert mocked_request.call_args == mock.call(
            method='GET', params=None,
            url='testapi/company/{}/'.format(ch_id), sso_session_id=None
        )

    @stub_request(url + 'ch_ID_00/', 'delete')
    def test_delete_company_by_ch_id(self, stub):
        ch_id = 'ch_ID_00'
        response = self.client.delete_company_by_ch_id(ch_id=ch_id)
        request = stub.request_history[0]
        assert request.url == response.url

    def test_delete_company_should_return_none_on_missing_ch_id(self):
        response = self.client.delete_company_by_ch_id(ch_id=None)
        assert response is None

    def test_delete_company_should_return_none_on_empty_ch_id(self):
        response = self.client.delete_company_by_ch_id(ch_id='')
        assert response is None

    @mock.patch('directory_api_client.base.BaseAPIClient.request')
    def test_delete_company_should_not_make_any_request_on_empty_ch_id(
            self, mocked_request):
        self.client.delete_company_by_ch_id(ch_id='')
        assert mocked_request.call_count == 0

    @mock.patch('directory_api_client.base.BaseAPIClient.request')
    def test_delete_company_should_not_make_any_request_on_no_ch_id(
            self, mocked_request):
        self.client.delete_company_by_ch_id(ch_id=None)
        assert mocked_request.call_count == 0

    @mock.patch('directory_api_client.base.BaseAPIClient.request')
    def test_delete_company(self, mocked_request):
        ch_id = '12345678'
        self.client.delete_company_by_ch_id(ch_id=ch_id)

        assert mocked_request.call_count == 1
        assert mocked_request.call_args == mock.call(
            method='DELETE', sso_session_id=None,
            url='testapi/company/{}/'.format(ch_id)
        )

    @given(ch_id=text(max_size=8))
    @hypothesis_settings(max_examples=95, deadline=1000)
    def test_get_company_by_ch_id_with_hypothesis(self, ch_id):
        response = self.client.get_company_by_ch_id(ch_id=ch_id)
        if ch_id:
            assert response.status_code == 404
        else:
            assert response is None

    @given(ch_id=text(max_size=8))
    @hypothesis_settings(max_examples=95, deadline=1000)
    def test_delete_company_by_ch_id_with_hypothesis(self, ch_id):
        response = self.client.delete_company_by_ch_id(ch_id=ch_id)
        if ch_id:
            assert response.status_code == 404
        else:
            assert response is None

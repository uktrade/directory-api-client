from unittest import mock, TestCase

from tests import stub_request

from directory_api_client.testapiclient import DirectoryTestAPIClient


class DirectoryTestAPIClientTest(TestCase):

    url_get_company = 'http://test.uk/testapi/company/'
    url_get_published_companies = 'http://test.uk/testapi/companies/published/'

    def setUp(self):
        self.base_url = 'http://test.uk'
        self.key = 'test'
        self.client = DirectoryTestAPIClient(
            base_url=self.base_url,
            api_key=self.key,
            sender_id='test',
            timeout=5,
        )

    def test_client_setup(self):
        assert isinstance(self.client, DirectoryTestAPIClient)
        assert self.client.base_url == self.base_url
        assert self.client.request_signer.secret == self.key

    def test_client_endpoints_urljoin(self):
        """urljoin replaces base_url's path if endpoints start with with / """
        for endpoint in self.client.endpoints.values():
            assert not endpoint.startswith('/')

    @stub_request(url_get_company + '12345678/', 'get')
    def test_get_company_by_ch_id(self, stub):
        ch_id = '12345678'
        response = self.client.get_company_by_ch_id(ch_id=ch_id)
        request = stub.request_history[0]
        assert request.url == response.url

    @stub_request(url_get_company + 'None/', 'get', 404)
    def test_get_company_should_return_404_on_missing_ch_id(self, stub):
        response = self.client.get_company_by_ch_id(ch_id=None)
        assert response.status_code == 404

    @stub_request(url_get_company, 'get', 404)
    def test_get_company_should_return_404_on_empty_ch_id(self, stub):
        response = self.client.get_company_by_ch_id(ch_id='')
        assert response.status_code == 404

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_get_company_should_make_request_on_empty_ch_id(
            self, mocked_request):
        self.client.get_company_by_ch_id(ch_id='')
        assert mocked_request.call_count == 1

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_get_company_should_make_request_on_no_ch_id(self, mocked_request):
        self.client.get_company_by_ch_id(ch_id=None)
        assert mocked_request.call_count == 1

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_get_company(self, mocked_request):
        ch_id = '12345678'
        self.client.get_company_by_ch_id(ch_id=ch_id)

        assert mocked_request.call_count == 1
        assert mocked_request.call_args == mock.call(
            method='GET',
            params=None,
            url='testapi/company/{}/'.format(ch_id),
            authenticator=mock.ANY,
            cache_control=None,
        )

    @stub_request(url_get_company + 'ch_ID_00/', 'delete')
    def test_delete_company_by_ch_id(self, stub):
        ch_id = 'ch_ID_00'
        response = self.client.delete_company_by_ch_id(ch_id=ch_id)
        request = stub.request_history[0]
        assert request.url == response.url

    @stub_request(url_get_company + 'None/', 'delete', 404)
    def test_delete_company_should_return_404_on_missing_ch_id(self, stub):
        response = self.client.delete_company_by_ch_id(ch_id=None)
        assert response.status_code == 404

    @stub_request(url_get_company, 'delete', 404)
    def test_delete_company_should_return_404_on_empty_ch_id(self, stub):
        response = self.client.delete_company_by_ch_id(ch_id='')
        assert response.status_code == 404

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_delete_company_should_make_request_on_empty_ch_id(
            self, mocked_request):
        self.client.delete_company_by_ch_id(ch_id='')
        assert mocked_request.call_count == 1

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_delete_company_should_make_request_on_no_ch_id(
            self, mocked_request):
        self.client.delete_company_by_ch_id(ch_id=None)
        assert mocked_request.call_count == 1

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_delete_company(self, mocked_request):
        ch_id = '12345678'
        self.client.delete_company_by_ch_id(ch_id=ch_id)

        assert mocked_request.call_count == 1
        assert mocked_request.call_args == mock.call(
            method='DELETE',
            url='testapi/company/{}/'.format(ch_id),
            authenticator=mock.ANY,
        )

    @stub_request(url_get_published_companies, 'get')
    def test_get_published_companies_without_optional_parameters(self, stub):
        response = self.client.get_published_companies()
        request = stub.request_history[0]
        assert request.url == response.url

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_get_published_companies_check_request(self, mocked_request):
        self.client.get_published_companies()
        assert mocked_request.call_count == 1
        assert mocked_request.call_args == mock.call(
            method='GET',
            params={},
            url='testapi/companies/published/',
            authenticator=mock.ANY,
            cache_control=None,
        )

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_get_published_companies_with_both_filters(
            self, mocked_request):
        limit = 10
        minimal_number_of_sectors = 5
        self.client.get_published_companies(
            limit=limit, minimal_number_of_sectors=minimal_number_of_sectors)
        expected_params = {
            'limit': limit,
            'minimal_number_of_sectors': minimal_number_of_sectors
        }
        assert mocked_request.call_count == 1
        assert mocked_request.call_args == mock.call(
            method='GET',
            params=expected_params,
            url='testapi/companies/published/',
            authenticator=mock.ANY,
            cache_control=None,
        )

    @mock.patch('directory_client_core.base.AbstractAPIClient.request')
    def test_get_published_companies_with_one_filter(
            self, mocked_request):
        minimal_number_of_sectors = 5
        self.client.get_published_companies(
            minimal_number_of_sectors=minimal_number_of_sectors)
        expected_params = {
            'minimal_number_of_sectors': minimal_number_of_sectors
        }
        assert mocked_request.call_count == 1
        assert mocked_request.call_args == mock.call(
            method='GET',
            params=expected_params,
            url='testapi/companies/published/',
            authenticator=mock.ANY,
            cache_control=None,
        )

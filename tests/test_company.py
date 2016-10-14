from unittest import TestCase

from tests import stub_request

from exportdirectory.company import CompanyAPIClient


class CompanyAPIClientTest(TestCase):

    def setUp(self):
        self.client = CompanyAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/company/1/', 'patch')
    def test_update_profile(self, stub):
        data = {'key': 'value'}
        self.client.update_profile(id=1, data=data)
        assert stub.request_history[0].json() == data

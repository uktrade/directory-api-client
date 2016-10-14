from unittest import TestCase

import requests

from tests import stub_request
from exportdirectory.base import BaseAPIClient


class BaseAPIClientTest(TestCase):

    def setUp(self):
        self.client = BaseAPIClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/test', 'post')
    def test_request(self, stub):
        self.client.request("POST", 'test', data='data')

    def test_sign_request(self):
        url = 'https://example.com'
        prepared_request = requests.Request(
            "POST", url, data='data'
        ).prepare()

        self.client.sign_request(
            api_key='test',
            url=url,
            prepared_request=prepared_request,
        )

    @stub_request('https://example.com', 'post')
    def test_send(self, stub):
        self.client.send(
            api_key='test', method="POST", url='https://example.com'
        )

    @stub_request('https://example.com/thing/', 'patch')
    def test_patch(self, stub):
        data = {'key': 'value'}
        self.client.patch(url='thing/', data=data)
        request = stub.request_history[0]
        assert request.json() == data
        assert request.headers['Content-type'] == 'application/json'

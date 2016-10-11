from unittest import TestCase

import requests

from exportdirectory.base import BaseAPIClient
from tests import mock_requests


class BaseAPIClientTest(TestCase):

    def setUp(self):
        self.client = BaseAPIClient(
            base_url='https://example.com', api_key='test'
        )

    def test_request(self):
        with mock_requests():
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

    def test_send(self):
        with mock_requests():
            self.client.send(
                api_key='test', method="POST", url='https://example.com'
            )

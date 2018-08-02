from unittest import TestCase

from tests import stub_request

from directory_api_client.notifications import NotificationsAPIClient


class NotificationsAPIClientTestCase(TestCase):

    def setUp(self):
        self.client = NotificationsAPIClient(
            base_url='https://e.com',
            api_key='test',
            sender_id='test',
            timeout=5,
        )

    @stub_request('https://e.com/notifications/anonymous-unsubscribe/', 'post')
    def test_anonymous_unsubscribe(self, stub):
        self.client.anonymous_unsubscribe(signed_email_address='a@b.com:1234')

        request = stub.request_history[0]
        assert request.json() == {'email': 'a@b.com:1234'}

from directory_api_client.base import BaseAPIClient
from directory_api_client.company import CompanyAPIClient
from directory_api_client.registration import EnrolmentAPIClient
from directory_api_client.user import UserAPIClient


class DirectoryAPIClient(BaseAPIClient):

    def __init__(self, base_url=None, api_key=None):
        super(DirectoryAPIClient, self).__init__(base_url, api_key)

        self.registration = EnrolmentAPIClient(base_url, api_key)
        self.company = CompanyAPIClient(base_url, api_key)
        self.user = UserAPIClient(base_url, api_key)
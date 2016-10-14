from exportdirectory.base import BaseAPIClient
from exportdirectory.company import CompanyAPIClient
from exportdirectory.registration import RegistrationAPIClient
from exportdirectory.user import UserAPIClient


class DirectoryAPIClient(BaseAPIClient):

    def __init__(self, base_url=None, api_key=None):
        super(DirectoryAPIClient, self).__init__(base_url, api_key)

        self.registration = RegistrationAPIClient(base_url, api_key)
        self.company = CompanyAPIClient(base_url, api_key)
        self.user = UserAPIClient(base_url, api_key)

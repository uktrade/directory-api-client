from directory_client_core.authentication import SessionSSOAuthenticator
from directory_api_client.base import AbstractAPIClient


url_user_location_create = '/personalisation/user-location/'
url_events = '/personalisation/events/'
url_export_opportunities = '/personalisation/export-opportunities/'


class PersonalisationAPIClient(AbstractAPIClient):
    authenticator = SessionSSOAuthenticator

    def user_location_create(self, sso_session_id, data):
        return self.post(url=url_user_location_create, data=data, authenticator=self.authenticator(sso_session_id))

    def events(self, sso_session_id, lat='', lng=''):
        return self.get(url=url_events, params={
          'sso_id': sso_session_id,
          'lat': lat,
          'lng': lng
        }, authenticator=self.authenticator(sso_session_id))

    def export_opportunities(self, sso_session_id):
        return self.get(url=url_export_opportunities, params={
          'sso_id': sso_session_id
        }, authenticator=self.authenticator(sso_session_id))

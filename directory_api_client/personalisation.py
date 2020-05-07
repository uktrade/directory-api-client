from directory_client_core.authentication import SessionSSOAuthenticator
from directory_api_client.base import AbstractAPIClient
import urllib

url_user_location_create = '/personalisation/user-location/'
url_events = '/personalisation/events/'
url_export_opportunities = '/personalisation/export-opportunities/?{}'
url_recommended_countries = '/personalisation/recommended-countries/'


class PersonalisationAPIClient(AbstractAPIClient):
    authenticator = SessionSSOAuthenticator

    def user_location_create(self, sso_session_id, data):
        return self.post(
            url=url_user_location_create,
            data=data,
            authenticator=self.authenticator(sso_session_id)
        )

    def events_by_location_list(self, sso_session_id, lat='', lng=''):
        return self.get(url=url_events, params={
          'lat': lat,
          'lng': lng
        }, authenticator=self.authenticator(sso_session_id))

    def export_opportunities_by_relevance_list(
        self, sso_session_id, query_params
    ):
        return self.get(
            url=url_export_opportunities.format(
                urllib.parse.urlencode(query_params)
            ),
            authenticator=self.authenticator(sso_session_id)
        )

    def recommended_countries_by_sector(
        self, sso_session_id, sector=''
    ):
        return self.get(
            url=url_recommended_countries, params={'sector': sector, }, authenticator=self.authenticator(sso_session_id)
        )

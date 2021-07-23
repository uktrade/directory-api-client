from directory_client_core.authentication import SessionSSOAuthenticator

from directory_api_client.base import AbstractAPIClient

url_user_location_create = '/personalisation/user-location/'
url_events = '/personalisation/events/'
url_export_opportunities = '/personalisation/export-opportunities/?s={}'
url_recommended_countries = '/personalisation/recommended-countries/'
url_user_product = '/personalisation/user-products/'


class PersonalisationAPIClient(AbstractAPIClient):
    authenticator = SessionSSOAuthenticator

    def user_location_create(self, sso_session_id, data):
        return self.post(url=url_user_location_create, data=data, authenticator=self.authenticator(sso_session_id))

    def events_by_location_list(self, sso_session_id, lat='', lng=''):
        return self.get(
            url=url_events, params={'lat': lat, 'lng': lng}, authenticator=self.authenticator(sso_session_id)
        )

    def export_opportunities_by_relevance_list(self, sso_session_id, search_term=''):
        return self.get(
            url=url_export_opportunities.format(search_term), authenticator=self.authenticator(sso_session_id)
        )

    def recommended_countries_by_sector(self, sso_session_id, sector=''):
        return self.get(
            url=url_recommended_countries,
            params={
                'sector': sector,
            },
            authenticator=self.authenticator(sso_session_id),
        )

    def get_user_products(self, sso_session_id):
        return self.get(url=url_user_product, authenticator=self.authenticator(sso_session_id))

    def add_update_user_product(self, sso_session_id, data):
        return self.post(url=url_user_product, data=data, authenticator=self.authenticator(sso_session_id))

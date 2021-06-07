import pytest

from directory_api_client.dataservices import DataServicesAPIClient


@pytest.fixture
def client():
    return DataServicesAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_get_country_data_by_country(client, requests_mock):
    url = 'https://example.com/dataservices/country-data/'
    requests_mock.get(url)
    client.get_country_data_by_country(countries=['FR', 'BE'], fields=['TestModel'])
    assert requests_mock.last_request.url == f'{url}?countries=FR&countries=BE&fields=TestModel'


def test_get_cia_world_factbook_data(client, requests_mock):
    url = 'https://example.com/dataservices/cia-factbook-data/?country=China&data_key=government%2C+languages'
    requests_mock.get(url)
    client.get_cia_world_factbook_data(country='China', data_key='government, languages')

    assert requests_mock.last_request.url == url


def test_get_population_data(client, requests_mock):
    url = 'https://example.com/dataservices/population-data/?country=China&target_ages=0-20&target_ages=21-35'
    requests_mock.get(url)
    client.get_population_data(country='China', target_ages=['0-20', '21-35'])

    assert requests_mock.last_request.url == url


def test_get_population_data_by_country(client, requests_mock):
    url = 'https://example.com/dataservices/population-data-by-country/?countries=Germany'
    requests_mock.get(url)
    client.get_population_data_by_country(countries='Germany')

    assert requests_mock.last_request.url == url


def test_get_society_data_by_country(client, requests_mock):
    url = 'https://example.com/dataservices/society-data-by-country/?countries=Germany'
    requests_mock.get(url)
    client.get_society_data_by_country(countries='Germany')

    assert requests_mock.last_request.url == url


def test_get_last_year_import_data_by_country(client, requests_mock):
    url = 'https://example.com/dataservices/lastyearimportdatabycountry/'
    requests_mock.get(url)
    client.get_last_year_import_data_by_country(countries=['GE', 'BE'], commodity_code=123456)

    assert requests_mock.last_request.url == f'{url}?commodity_code=123456&countries=GE&countries=BE'


def test_suggested_countries_by_hs_code(requests_mock, client):
    url = 'https://example.com/dataservices/suggested-countries/?hs_code=1'
    requests_mock.get(url)
    hs_code = {'1'}
    client.suggested_countries_by_hs_code(hs_code=hs_code)

    assert requests_mock.last_request.url == url


def test_trading_blocs_by_country(requests_mock, client):
    url = 'https://example.com/dataservices/trading-blocs/?iso2=IN'
    requests_mock.get(url)
    iso2 = {'IN'}
    client.trading_blocs_by_country(iso2=iso2)

    assert requests_mock.last_request.url == url


def test_get_trade_barriers_by_countries_sectors(requests_mock, client):
    url = 'https://example.com/dataservices/trade-barriers/'
    requests_mock.get(url)
    client.get_trade_barriers(countries=['GE', 'BE'], sectors=['Automotive', 'Technology'])

    assert requests_mock.last_request.url == f'{url}?sectors=Automotive&sectors=Technology&countries=GE&countries=BE'

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


def test_get_corruption_perceptions_index(client, requests_mock):
    url = 'https://example.com/dataservices/corruption-perceptions-index/CHN/'
    requests_mock.get(url)
    client.get_corruption_perceptions_index(country_code='CHN')

    assert requests_mock.last_request.url == url


def test_get_easeofdoingbusiness(client, requests_mock):
    url = 'https://example.com/dataservices/easeofdoingbusiness/CHN/'
    requests_mock.get(url)
    client.get_ease_of_doing_business(country_code='CHN')

    assert requests_mock.last_request.url == url


def test_get_lastyearimportdata(requests_mock, client):
    url = 'https://example.com/dataservices/lastyearimportdata/?commodity_code=1234&country=China'
    requests_mock.get(url)
    client.get_last_year_import_data(commodity_code=1234, country='China')

    assert requests_mock.last_request.url == url


def test_get_historicalimportdata(requests_mock, client):
    url = 'https://example.com/dataservices/historicalimportdata/?commodity_code=1234&country=China'
    requests_mock.get(url)
    client.get_historical_import_data(commodity_code=1234, country='China')

    assert requests_mock.last_request.url == url


def test_get_world_exconomic_outlook_data(client, requests_mock):
    url = 'https://example.com/dataservices/world-economic-outlook/CHN/'
    requests_mock.get(url)
    client.get_world_economic_outlook_data(country_code='CHN')

    assert requests_mock.last_request.url == url


def test_get_country_data(client, requests_mock):
    url = 'https://example.com/dataservices/country-data/China/'
    requests_mock.get(url)
    client.get_country_data(country='China')

    assert requests_mock.last_request.url == url


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


def test_get_last_year_import_data_from_uk(client, requests_mock):
    url = 'https://example.com/dataservices/lastyearimportdatafromuk/?commodity_code=123456&country=Germany'
    requests_mock.get(url)
    client.get_last_year_import_data_from_uk(country='Germany', commodity_code=123456)

    assert requests_mock.last_request.url == url


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

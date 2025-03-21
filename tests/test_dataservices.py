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


def test_get_markets_data(client, requests_mock):
    url = 'https://example.com/dataservices/markets/'
    requests_mock.get(url)
    client.get_markets_data()
    assert requests_mock.last_request.url == url


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


def test_get_market_trends_by_country(requests_mock, client):
    url = 'https://example.com/dataservices/uk-market-trends/'
    requests_mock.get(url)
    client.get_market_trends_by_country(iso2='FR', from_year=2020)

    assert requests_mock.last_request.url == f'{url}?iso2=FR&from_year=2020'

    client.get_market_trends_by_country(iso2='FR')

    assert requests_mock.last_request.url == f'{url}?iso2=FR'


def test_get_trade_highlights_by_country(requests_mock, client):
    url = 'https://example.com/dataservices/uk-trade-highlights/'
    requests_mock.get(url)
    client.get_trade_highlights_by_country(iso2='FR')

    assert requests_mock.last_request.url == f'{url}?iso2=FR'


def test_get_commodity_exports_data_by_country(requests_mock, client):
    url = 'https://example.com/dataservices/commodity-exports-data-by-country/'
    requests_mock.get(url)
    client.get_commodity_exports_data_by_country(iso2='FR')

    assert requests_mock.last_request.url == f'{url}?iso2=FR'


def test_get_top_five_services(requests_mock, client):
    url = 'https://example.com/dataservices/top-five-services/'
    requests_mock.get(url)
    client.get_top_five_services_by_country(iso2='FR')

    assert requests_mock.last_request.url == f'{url}?iso2=FR'


def test_get_top_five_goods(requests_mock, client):
    url = 'https://example.com/dataservices/top-five-goods/'
    requests_mock.get(url)
    client.get_top_five_goods_by_country(iso2='FR')

    assert requests_mock.last_request.url == f'{url}?iso2=FR'


def test_get_economic_highlights(requests_mock, client):
    url = 'https://example.com/dataservices/economic-highlights/'
    requests_mock.get(url)
    client.get_economic_highlights_by_country(iso2='FR')
    assert requests_mock.last_request.url == f'{url}?iso2=FR'


def test_list_uk_free_trade_agreements(requests_mock, client):
    url = 'https://example.com/dataservices/uk-free-trade-agreements/'
    requests_mock.get(url)
    client.list_uk_free_trade_agreements()
    assert requests_mock.last_request.url == url


def test_business_cluster_information_sic_only(requests_mock, client):
    url = 'https://example.com/dataservices/business-cluster-information-by-sic/'
    requests_mock.get(url)
    client.get_business_cluster_information_by_sic(sic_code='12345')
    assert requests_mock.last_request.url == f'{url}?sic_code=12345'


def test_business_cluster_information_sic_and_geo(requests_mock, client):
    url = 'https://example.com/dataservices/business-cluster-information-by-sic/'
    requests_mock.get(url)
    client.get_business_cluster_information_by_sic(sic_code='12345', geo_code='AB0001,XY12345')
    assert requests_mock.last_request.url == f'{url}?sic_code=12345&geo_code=AB0001%2CXY12345'


def test_business_cluster_information_dbt_sector_only(requests_mock, client):
    url = 'https://example.com/dataservices/business-cluster-information-by-dbt-sector/'
    requests_mock.get(url)
    client.get_business_cluster_information_by_dbt_sector(dbt_sector_name='Financial and professional services')
    assert requests_mock.last_request.url == f'{url}?dbt_sector_name=Financial+and+professional+services'


def test_business_cluster_information_dbt_sector_and_geo(requests_mock, client):
    url = 'https://example.com/dataservices/business-cluster-information-by-dbt-sector/'
    requests_mock.get(url)
    client.get_business_cluster_information_by_dbt_sector(
        dbt_sector_name='Financial and professional services', geo_code='AB0001,XY12345'
    )
    assert (
        requests_mock.last_request.url
        == f'{url}?dbt_sector_name=Financial+and+professional+services&geo_code=AB0001%2CXY12345'
    )


def test_eyb_salary_vertical(requests_mock, client):
    url = 'https://example.com/dataservices/eyb-salary-data/'
    requests_mock.get(url)
    client.get_eyb_salary_data(vertical='Advanced Engineering')
    assert requests_mock.last_request.url == f'{url}?vertical=Advanced+Engineering'


def test_eyb_salary_geo_description_vertical(requests_mock, client):
    url = 'https://example.com/dataservices/eyb-salary-data/'
    requests_mock.get(url)
    client.get_eyb_salary_data(vertical='Aerospace', geo_description='London')
    assert requests_mock.last_request.url == f'{url}?vertical=Aerospace&geo_description=London'


def test_eyb_salary_geo_description_vertical_professional_level(requests_mock, client):
    url = 'https://example.com/dataservices/eyb-salary-data/'
    requests_mock.get(url)
    client.get_eyb_salary_data(vertical='Aerospace', professional_level='Entry-level', geo_description='London')
    assert (
        requests_mock.last_request.url
        == f'{url}?vertical=Aerospace&professional_level=Entry-level&geo_description=London'
    )


def test_eyb_commercial_rent_data_geo_description(requests_mock, client):
    url = 'https://example.com/dataservices/eyb-commercial-rent-data/'
    requests_mock.get(url)
    client.get_eyb_commercial_rent_data(geo_description='London')
    assert requests_mock.last_request.url == f'{url}?geo_description=London'


def test_eyb_commercial_rent_data_geo_description_vertical(requests_mock, client):
    url = 'https://example.com/dataservices/eyb-commercial-rent-data/'
    requests_mock.get(url)
    client.get_eyb_commercial_rent_data(geo_description='London', vertical='Industrial')
    assert requests_mock.last_request.url == f'{url}?geo_description=London&vertical=Industrial'


def test_eyb_commercial_rent_data_geo_description_vertical_sub_vertical(requests_mock, client):
    url = 'https://example.com/dataservices/eyb-commercial-rent-data/'
    requests_mock.get(url)
    client.get_eyb_commercial_rent_data(geo_description='London', vertical='Industrial', sub_vertical='Large Warehouse')
    assert (
        requests_mock.last_request.url
        == f'{url}?geo_description=London&vertical=Industrial&sub_vertical=Large+Warehouse'
    )


def test_dbt_sectors(requests_mock, client):
    url = 'https://example.com/dataservices/dbt-sector/'
    requests_mock.get(url)
    client.get_dbt_sectors()
    assert requests_mock.last_request.url == f'{url}'


def test_gva_bandings(requests_mock, client):
    url = 'https://example.com/dataservices/sector-gva-value-band/'
    requests_mock.get(url)
    client.get_gva_bandings(full_sector_name='Aerospace')
    assert requests_mock.last_request.url == f'{url}?full_sector_name=Aerospace'


def test_(requests_mock, client):
    url = 'https://example.com/dataservices/all-sectors-gva-value-bands/'
    requests_mock.get(url)
    client.get_all_sectors_gva_value_bands()
    assert requests_mock.last_request.url == f'{url}'


def test_countries_territories_regions(requests_mock, client):
    url = 'https://example.com/dataservices/countries-territories-regions/'
    requests_mock.get(url)
    client.get_all_countries_territories_regions()
    assert requests_mock.last_request.url == url


def test_countries_territories_regions_single_country(requests_mock, client):
    url = 'https://example.com/dataservices/country-territory-region/FR'
    requests_mock.get(url)
    client.get_country_territory_region(iso2_code='fr')
    assert requests_mock.last_request.url == url


def test_get_news_content(requests_mock, client):
    url = 'https://example.com/dataservices/news-content/'
    requests_mock.get(url)
    client.get_news_content()
    assert requests_mock.last_request.url == url


def test_support_by_postcode(requests_mock, client):
    url = 'https://example.com/dataservices/growth-hubs-commerce-chambers/'
    requests_mock.get(url)
    client.get_local_support_by_postcode(postcode='SW1A1AA')
    assert requests_mock.last_request.url == f'{url}?postcode=SW1A1AA'

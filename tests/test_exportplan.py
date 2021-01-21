import pytest

from directory_api_client.exportplan import ExportPlanAPIClient


@pytest.fixture
def client():
    return ExportPlanAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_exportplan_list(client, requests_mock):
    url = 'https://example.com/exportplan/company-export-plan/'
    requests_mock.get(url)

    client.exportplan_list(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_exportplan_retrieve(client, requests_mock):
    url = 'https://example.com/exportplan/company-export-plan/123/'
    requests_mock.get(url)
    client.exportplan_detail(id='123', sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_exportplan_create(requests_mock, client):
    url = 'https://example.com/exportplan/company-export-plan/'
    requests_mock.post(url)
    client.exportplan_create(sso_session_id=2, data={'export_commodity_codes': ['101.102.1']})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'export_commodity_codes': ['101.102.1']}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_exportplan_update(requests_mock, client):
    url = 'https://example.com/exportplan/company-export-plan/123/'
    requests_mock.patch(url)
    client.exportplan_update(sso_session_id=2, id=123, data={'export_commodity_codes': ['101.102.1']})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'export_commodity_codes': ['101.102.1']}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_exportplan_objectives_list(client, requests_mock):
    url = 'https://example.com/exportplan/company-objectives/'
    requests_mock.get(url)

    client.exportplan_objectives_list(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_exportplan_objectives_retrieve(client, requests_mock):
    url = 'https://example.com/exportplan/company-objectives/123/'
    requests_mock.get(url)
    client.exportplan_objectives_detail(id='123', sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_exportplan_objectives_create(requests_mock, client):
    url = 'https://example.com/exportplan/company-objectives/'
    requests_mock.post(url)
    client.exportplan_objectives_create(sso_session_id=2, data={'description': 'new objective'})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'description': 'new objective'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_exportplan_objectives_update(requests_mock, client):
    url = 'https://example.com/exportplan/company-objectives/123/'
    requests_mock.patch(url)
    client.exportplan_objectives_update(sso_session_id=2, id=123, data={'description': 'new objective'})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'description': 'new objective'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_exportplan_objectives_delete(requests_mock, client):
    url = 'https://example.com/exportplan/company-objectives/123/'
    requests_mock.delete(url)
    client.exportplan_objectives_delete(sso_session_id=2, id=123)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_route_to_market_list(client, requests_mock):
    url = 'https://example.com/exportplan/route-to-markets/'
    requests_mock.get(url)

    client.route_to_market_list(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_route_to_market_retrieve(client, requests_mock):
    url = 'https://example.com/exportplan/route-to-markets/123/'
    requests_mock.get(url)
    client.route_to_market_detail(id='123', sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_route_to_market_create(requests_mock, client):
    url = 'https://example.com/exportplan/route-to-markets/'
    requests_mock.post(url)
    client.route_to_market_create(sso_session_id=2, data={'description': 'new route'})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'description': 'new route'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_route_to_market_update(requests_mock, client):
    url = 'https://example.com/exportplan/route-to-markets/123/'
    requests_mock.patch(url)
    client.route_to_market_update(sso_session_id=2, id=123, data={'description': 'new route'})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'description': 'new route'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_route_to_market_delete(requests_mock, client):
    url = 'https://example.com/exportplan/route-to-markets/123/'
    requests_mock.delete(url)
    client.route_to_market_delete(sso_session_id=2, id=123)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_target_market_documents_list(client, requests_mock):
    url = 'https://example.com/exportplan/target-market-documents/'
    requests_mock.get(url)

    client.target_market_documents_list(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_target_market_documents_retrieve(client, requests_mock):
    url = 'https://example.com/exportplan/target-market-documents/123/'
    requests_mock.get(url)
    client.target_market_documents_detail(id='123', sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_target_market_documents_create(requests_mock, client):
    url = 'https://example.com/exportplan/target-market-documents/'
    requests_mock.post(url)
    client.target_market_documents_create(sso_session_id=2, data={'document_name': 'new doc'})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'document_name': 'new doc'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_target_market_documents_update(requests_mock, client):
    url = 'https://example.com/exportplan/target-market-documents/123/'
    requests_mock.patch(url)
    client.target_market_documents_update(sso_session_id=2, id=123, data={'document_name': 'new doc'})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'document_name': 'new doc'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_target_market_documents_delete(requests_mock, client):
    url = 'https://example.com/exportplan/target-market-documents/123/'
    requests_mock.delete(url)
    client.target_market_documents_delete(sso_session_id=2, id=123)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_funding_credit_options_list(client, requests_mock):
    url = 'https://example.com/exportplan/funding-credit-options/'
    requests_mock.get(url)

    client.funding_credit_options_list(sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_funding_credit_options__retrieve(client, requests_mock):
    url = 'https://example.com/exportplan/funding-credit-options/123/'
    requests_mock.get(url)
    client.funding_credit_options_detail(id='123', sso_session_id=2)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_funding_credit_options__create(requests_mock, client):
    url = 'https://example.com/exportplan/funding-credit-options/'
    requests_mock.post(url)
    client.funding_credit_options_create(sso_session_id=2, data={'document_name': 'new doc'})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'document_name': 'new doc'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_funding_credit_options__update(requests_mock, client):
    url = 'https://example.com/exportplan/funding-credit-options/123/'
    requests_mock.patch(url)
    client.funding_credit_options_update(sso_session_id=2, id=123, data={'document_name': 'new doc'})

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'document_name': 'new doc'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_funding_credit_options__delete(requests_mock, client):
    url = 'https://example.com/exportplan/funding-credit-options/123/'
    requests_mock.delete(url)
    client.funding_credit_options_delete(sso_session_id=2, id=123)

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'

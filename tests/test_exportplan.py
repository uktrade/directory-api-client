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


def test_model_object_create_retrieve(client, requests_mock):
    url = 'https://example.com/exportplan/export-plan-model-object-detail/123/mymodel/'
    requests_mock.get(url)
    client.model_object_detail(id='123', sso_session_id=2, model_name='mymodel')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_model_object_create(requests_mock, client):
    url = 'https://example.com/exportplan/export-plan-model-object-list-create/'
    requests_mock.post(url)
    client.model_object_create(sso_session_id=2, data={'document_name': 'new doc'}, model_name='mymodel')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'document_name': 'new doc', 'model_name': 'mymodel'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_model_object_update(requests_mock, client):
    url = 'https://example.com/exportplan/export-plan-model-object-update-delete/123/'
    requests_mock.patch(url)
    client.model_object_update(sso_session_id=2, id=123, data={'document_name': 'new doc'}, model_name='mymodel')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.json() == {'document_name': 'new doc', 'model_name': 'mymodel'}
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'


def test_model_object_delete(requests_mock, client):
    url = 'https://example.com/exportplan/export-plan-model-object-update-delete/123/'
    requests_mock.delete(url)
    client.model_object_delete(sso_session_id=2, id=123, model_name='mymodel')

    assert requests_mock.last_request.url == url
    assert requests_mock.last_request.headers['Authorization'] == 'SSO_SESSION_ID 2'

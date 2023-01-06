import pytest

from directory_api_client.survey import SurveyAPIClient


@pytest.fixture
def client():
    return SurveyAPIClient(
        base_url='https://example.com',
        api_key='test',
        sender_id='test',
        timeout=5,
    )


def test_get_survey_details(requests_mock, client):
    url = 'https://example.com/survey/123'
    requests_mock.get(url)
    client.get_survey_details(id='123')
    assert requests_mock.last_request.url == url


# Adding a change to test codecov

from django.urls import reverse
import pytest
from api_app.tests.factories import ValueFactory, PrincipleFactory


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.mark.django_db
class TestValues:
    def test_values_list_status(self, api_client):
        url = reverse('values_list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_values_list_create(self, api_client):
        url = reverse('values_list')
        response = api_client.post(url)
        assert response.status_code == 405

    def test_value_in_list(self, api_client):
        values = ValueFactory.create_batch(4)
        url = reverse('values_list')
        response = api_client.get(url)
        assert len(response.data) == 4
        assert response.data[0].get("text") == "Value 1"

@pytest.mark.django_db
class TestPrinciple:
    def test_principle_list_status(self, api_client):
        url = reverse('principles_list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_principle_list_create(self, api_client):
        url = reverse('principles_list')
        response = api_client.post(url)
        assert response.status_code == 405

    def test_principle_list_value(self, api_client):
        url = reverse('principles_list')
        principles = PrincipleFactory.create_batch(12)
        response = api_client.get(url)
        assert len(response.data) == 12
        assert response.data[0].get("text") == 'Principle 1'


from api.api_client import APIClient
from pages.login_page import LoginPage

client = APIClient()

def test_get_users():
    response = client.get_users()
    assert response.status_code == 200

def test_create_post():
    data = {"title": "test", "body": "automation", "userId": 1}
    response = client.create_post(data)
    assert response.status_code == 201

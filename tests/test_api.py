# pip install requests
# pip install pytest-html
import pytest
import requests

BASE_URL = "https://reqres.in/api"

def test_get_users():
    # Test GET Request for users on page 2
    response = requests.get(f'{BASE_URL}/users?page=2')
    print(response.status_code)
    assert response.status_code == 200
    #print(response.json())
    assert "data" in response.json()









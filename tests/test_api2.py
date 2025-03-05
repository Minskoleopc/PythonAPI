import pytest
from api_utility import APIUtility  # Import the API Utility class

BASE_URL = "https://reqres.in/api"

@pytest.fixture
def api_client():
    """Fixture to provide API client instance"""
    return APIUtility(BASE_URL)

def test_get_users(api_client):
    """Test GET request for users page 2"""
    response = api_client.get("/users", params={"page": 2})
    
    assert response["status_code"] == 200
    assert "data" in response["data"]  # Ensure 'data' key exists
    assert isinstance(response["data"]["data"], list)  # Ensure data is a list
    assert len(response["data"]["data"]) > 0  # Ensure users exist

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6])
def test_get_single_user(api_client, user_id):
    """Test GET request for a single user"""
    response = api_client.get(f"/users/{user_id}")
    
    assert response["status_code"] == 200
    assert "data" in response["data"]
    assert response["data"]["data"]["id"] == user_id  # Validate user ID

def test_create_user(api_client):
    """Test POST request to create a user"""
    payload = {"name": "John Doe", "job": "QA Engineer"}
    response = api_client.post("/users", json=payload)
    
    assert response["status_code"] == 201
    assert "data" not in response  # POST response does not have a "data" field
    assert response["name"] == "John Doe"
    assert response["job"] == "QA Engineer"

def test_update_user(api_client):
    """Test PUT request to update user details"""
    payload = {"name": "Jane Doe", "job": "Senior QA"}
    response = api_client.put("/users/2", json=payload)
    
    assert response["status_code"] == 200
    assert response["data"]["name"] == "Jane Doe"
    assert response["data"]["job"] == "Senior QA"

def test_delete_user(api_client):
    """Test DELETE request for a user"""
    response = api_client.delete("/users/2")
    
    assert response["status_code"] == 204  # No content expected after deletion
    assert response["data"] is None  # Response data should be empty


import pytest
from starlette.testclient import TestClient
from app.server import karvaaa
from requests.auth import HTTPBasicAuth
import json
import randtest as rt
import numpy as np
from scipy.stats import chisquare


def test_randomness(texts):
    # Concatenate all texts into one long string
    concatenated_text = ' '.join(texts)
    words = concatenated_text.split()
    # Calculate the observed frequencies of each word
    observed_frequencies = np.array([words.count(word) for word in set(words)])
    # Calculate the expected frequencies assuming uniform distribution
    total_words = len(words)
    expected_frequencies = np.array([total_words / len(set(words))] * len(set(words)))
    chi2_stat, p_val = chisquare(observed_frequencies, f_exp=expected_frequencies)
    return p_val > 0.05 

@pytest.fixture
def client():
    """Create a TestClient instance for testing."""
    return TestClient(karvaaa)

def test_login(client):
    """Test the /chat/login endpoint."""
    user_data = {"username": "admin", "password": "@hjdhs5756U7YG"}
    # user_data = {"username": "test_user", "password": "test_password"}
    response = client.post("/chat/login", auth=HTTPBasicAuth(user_data['username'], user_data["password"]),)
    assert response.status_code == 200
    # Check the response content
    assert "session_id" in response.json()
    assert "existing_sessions" in response.json()

def test_logout(client):
    """Test the /chat/logout endpoint."""
    # Send a POST request to the endpoint
    response = client.post("/chat/logout?session_id=h20NCCrHaz")
    # Check the response status code
    assert response.status_code == 200
    assert response.json() == {"message": "Logout successful"}

def test_get_chat_unauthenticated(client):
    """Test the /chat/ endpoint without authentication."""
    # Send a GET request to the endpoint without session_id
    response = client.get("/chat/?user_input=test_input")
    # Check the response status code
    assert response.status_code == 401


def test_get_chat_authenticated(client):
    """Test the /chat/ endpoint with authentication."""
    user_data = {"username": "admin", "password": "@hjdhs5756U7YG"}
    response = client.post("/chat/login", auth=HTTPBasicAuth(user_data['username'], user_data["password"]))
    # Check if the login was successful and get the session_id
    assert response.status_code == 200
    data = response.json()
    assert "session_id" in data
    session_id = data['session_id']
    response = client.get(f"/chat/?user_input=ssss&session_id={session_id}")
    # Check the response status code
    assert response.status_code == 200

def test_get_chat_unauthorized(client):
    """Test the /chat/ endpoint with invalid session_id."""
    # Define test data
    invalid_session_id = "invalid_session_id"
    # Send a GET request to the endpoint with invalid session_id
    response = client.get(f"/chat/?user_input=test_input&session_id={invalid_session_id}")
    # Check the response status code
    assert response.status_code == 401

def test_get_chat_history_unauthenticated(client):
    """Test the /chat/history endpoint without authentication."""
    # Send a GET request to the endpoint without session_id
    response = client.get("/chat/history")
    # Check the response status code
    assert response.status_code == 401
    
def get_chat_randomness(client, user_input: str, session_id: str):
    response = client.get(f"/chat/?user_input={user_input}&session_id={session_id}")
    return json.loads(response.text)['response']

def test_get_chat_randomness(client):
    # Define the input space for the function
    user_data = {"username": "admin", "password": "@hjdhs5756U7YG"}
    # Send a POST request to the login endpoint to obtain session_id
    response = client.post("/chat/login", auth=HTTPBasicAuth(user_data['username'], user_data["password"]))
    # Check if the login was successful and get the session_id
    assert response.status_code == 200
    data = response.json()
    assert "session_id" in data
    session_id = data['session_id']
    # Set the number of iterations for testing
    iterations = 100
    # Run the test
    result = [get_chat_randomness(client, "hello", session_id) for _ in range(iterations)]
    randomness_result = test_randomness(result)
    print("Is the list of texts random?", randomness_result)
    assert randomness_result
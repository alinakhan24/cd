import pytest
from main import app  # Import the Flask app from app.py

@pytest.fixture
def client():
    """Creates a test client using Flask's test_client()"""
    app.config["TESTING"] = True  # Enable testing mode
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the '/' route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, world!"

def test_cow(client):
    """Test the '/cow' route"""
    response = client.get("/cow")
    assert response.status_code == 200
    assert response.data == b"MOoooOo!"

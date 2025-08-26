import requests
import json

# Test API endpoints
BASE_URL = "http://localhost:5000/api"

def test_health():
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Health check: {response.status_code} - {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_login():
    try:
        data = {
            "email": "john.smith@university.edu",
            "password": "password123"
        }
        response = requests.post(f"{BASE_URL}/auth/login", json=data)
        print(f"Login: {response.status_code} - {response.text}")
        if response.status_code == 200:
            return response.json().get('access_token')
        return None
    except Exception as e:
        print(f"Login failed: {e}")
        return None

def test_feedback(token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}/feedback", headers=headers)
        print(f"Feedback: {response.status_code} - {len(response.text)} chars")
        if response.status_code == 200:
            data = response.json()
            print(f"Feedback count: {len(data.get('feedback', []))}")
        return response.status_code == 200
    except Exception as e:
        print(f"Feedback test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing API endpoints...")
    
    # Test health
    if not test_health():
        print("Backend not responding")
        exit(1)
    
    # Test login
    token = test_login()
    if not token:
        print("Login failed")
        exit(1)
    
    # Test feedback
    if not test_feedback(token):
        print("Feedback endpoint failed")
        exit(1)
    
    print("All tests passed!")

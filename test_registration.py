import requests
import json

# Test registration endpoint
def test_registration():
    url = "http://localhost:5000/api/auth/register"
    
    # Test data
    test_user = {
        "name": "Test Teacher",
        "email": "test@example.com",
        "password": "password123",
        "role": "teacher",
        "department": "Computer Science",
        "subjects": ["Programming", "Database"]
    }
    
    try:
        print("Testing registration endpoint...")
        print(f"URL: {url}")
        print(f"Data: {json.dumps(test_user, indent=2)}")
        
        response = requests.post(url, json=test_user)
        
        print(f"\nResponse Status: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 201:
            print("✅ Registration successful!")
        else:
            print("❌ Registration failed!")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend server. Make sure it's running on port 5000.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_registration()

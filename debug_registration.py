#!/usr/bin/env python3
import requests
import json
import sys

def test_backend_connection():
    """Test if backend server is running"""
    try:
        response = requests.get("http://localhost:5000/api/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend server is running")
            return True
        else:
            print(f"❌ Backend server returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Backend server is not running. Start it with: python run.py")
        return False
    except Exception as e:
        print(f"❌ Error connecting to backend: {e}")
        return False

def test_registration():
    """Test registration with sample data"""
    url = "http://localhost:5000/api/auth/register"
    
    # Test with teacher data
    test_data = {
        "name": "Test Teacher",
        "email": "teacher@test.com",
        "password": "password123",
        "role": "teacher",
        "department": "Computer Science",
        "subjects": ["Programming"]
    }
    
    try:
        print("\n🧪 Testing registration endpoint...")
        response = requests.post(url, json=test_data, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 201:
            print("✅ Registration successful!")
            return True
        elif response.status_code == 409:
            print("⚠️  User already exists - try with different email")
            return True
        else:
            print("❌ Registration failed")
            return False
            
    except Exception as e:
        print(f"❌ Registration test failed: {e}")
        return False

def main():
    print("🔍 Debugging Registration Issues\n")
    
    # Test backend connection
    if not test_backend_connection():
        print("\n💡 Solution: Start your backend server first!")
        sys.exit(1)
    
    # Test registration
    if not test_registration():
        print("\n💡 Check backend logs for detailed error messages")
        sys.exit(1)
    
    print("\n✅ Registration system is working correctly!")

if __name__ == "__main__":
    main()

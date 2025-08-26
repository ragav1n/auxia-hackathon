#!/usr/bin/env python3

import requests
import json
import sys
import os

# Test API calls to debug dashboard data loading
def test_api_endpoints():
    base_url = "http://localhost:5000/api"
    
    # Test without authentication first
    print("Testing API endpoints...")
    
    try:
        # Test feedback endpoint
        print("\n1. Testing /api/feedback endpoint:")
        response = requests.get(f"{base_url}/feedback")
        print(f"Status: {response.status_code}")
        if response.status_code == 401:
            print("Authentication required - this is expected")
        else:
            print(f"Response: {response.text[:200]}...")
        
        # Test analytics endpoint
        print("\n2. Testing /api/analytics/overview endpoint:")
        response = requests.get(f"{base_url}/analytics/overview")
        print(f"Status: {response.status_code}")
        if response.status_code == 401:
            print("Authentication required - this is expected")
        else:
            print(f"Response: {response.text[:200]}...")
        
        # Test health endpoint
        print("\n3. Testing /api/health endpoint:")
        response = requests.get(f"{base_url}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend server. Is it running on port 5000?")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api_endpoints()

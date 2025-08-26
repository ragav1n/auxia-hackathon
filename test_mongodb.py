from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def test_mongodb_connection():
    try:
        # Get MongoDB URI from environment
        mongodb_uri = os.getenv('MONGODB_URI')
        print(f"Testing MongoDB connection...")
        print(f"URI: {mongodb_uri[:50]}...")  # Only show first 50 chars for security
        
        # Create client
        client = MongoClient(mongodb_uri)
        
        # Test connection
        db = client.get_database('faculty_feedback')
        
        # Try to ping the database
        client.admin.command('ping')
        print("✅ MongoDB connection successful!")
        
        # Test a simple operation
        result = db.users.count_documents({})
        print(f"✅ Current user count: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        return False

if __name__ == "__main__":
    test_mongodb_connection()

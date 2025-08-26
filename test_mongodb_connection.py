#!/usr/bin/env python3

import os
import pymongo
from dotenv import load_dotenv
from bson import ObjectId

def test_mongodb_connection():
    """Test MongoDB connection and check feedback data structure"""
    
    # Load environment variables
    load_dotenv()
    
    mongodb_uri = os.getenv('MONGODB_URI')
    if not mongodb_uri:
        print("ERROR: MONGODB_URI not found in environment variables")
        return False
    
    try:
        # Connect to MongoDB
        print(f"Connecting to MongoDB...")
        client = pymongo.MongoClient(mongodb_uri)
        
        # Test connection
        client.admin.command('ping')
        print("✅ MongoDB connection successful")
        
        # Get database
        db = client.get_default_database()
        print(f"Database name: {db.name}")
        
        # List collections
        collections = db.list_collection_names()
        print(f"Collections: {collections}")
        
        # Check feedback collection
        if 'feedback' not in collections:
            print("❌ 'feedback' collection not found")
            return False
        
        # Get feedback count
        feedback_count = db.feedback.count_documents({})
        print(f"Total feedback documents: {feedback_count}")
        
        if feedback_count == 0:
            print("❌ No feedback documents found")
            return False
        
        # Get sample document
        sample = db.feedback.find_one()
        if sample:
            print("\n📄 Sample document structure:")
            print(f"Document ID: {sample.get('_id')}")
            print(f"Keys: {list(sample.keys())}")
            
            # Check key fields
            faculty_id = sample.get('faculty_id')
            course_id = sample.get('course_id')
            student_id = sample.get('student_id')
            
            print(f"\n🔍 Key fields:")
            print(f"Faculty ID: {faculty_id}")
            print(f"Course ID: {course_id}")
            print(f"Student ID: {student_id}")
            
            # Check ratings structure
            ratings = sample.get('ratings', {})
            print(f"\n⭐ Ratings structure:")
            for rating_type, rating_data in ratings.items():
                print(f"  {rating_type}: {rating_data}")
            
            # Check overall structure
            overall = sample.get('overall', {})
            print(f"\n📊 Overall structure:")
            print(f"  Sentiment: {overall.get('sentiment')}")
            print(f"  Rating: {overall.get('overall_rating')}")
            
            # Check signals
            signals = sample.get('signals', {})
            print(f"\n🚦 Signals structure:")
            print(f"  Positive: {signals.get('positive_signals', [])}")
            print(f"  Pain points: {signals.get('pain_points', [])}")
            
        return True
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {str(e)}")
        return False
    
    finally:
        try:
            client.close()
        except:
            pass

if __name__ == "__main__":
    test_mongodb_connection()

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

try:
    client = pymongo.MongoClient(os.getenv('MONGODB_URI'))
    db = client.get_default_database()
    
    # Test connection
    client.admin.command('ping')
    print("MongoDB connected successfully")
    
    # Check collections
    collections = db.list_collection_names()
    print(f"Collections: {collections}")
    
    # Check feedback collection
    if 'feedback' in collections:
        count = db.feedback.count_documents({})
        print(f"Feedback documents: {count}")
        
        # Get sample document
        sample = db.feedback.find_one()
        if sample:
            print(f"Sample document keys: {list(sample.keys())}")
            print(f"Faculty ID: {sample.get('faculty_id')}")
            print(f"Course ID: {sample.get('course_id')}")
            
            # Check ratings structure
            ratings = sample.get('ratings', {})
            if ratings:
                print(f"Ratings keys: {list(ratings.keys())}")
                for key, value in ratings.items():
                    print(f"  {key}: {value}")
        else:
            print("No sample document found")
    else:
        print("Feedback collection not found")
        
except Exception as e:
    print(f"Error: {e}")

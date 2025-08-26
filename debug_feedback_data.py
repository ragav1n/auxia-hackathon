#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend'))

from app import create_app
from dotenv import load_dotenv
from bson import ObjectId

def debug_feedback_data():
    load_dotenv()
    app = create_app('development')
    
    with app.app_context():
        try:
            # Check sample feedback document structure
            sample = app.db.feedback.find_one()
            if sample:
                print("Sample feedback document structure:")
                for key, value in sample.items():
                    print(f"  {key}: {type(value)} = {value}")
                
                print(f"\nFaculty ID field: {sample.get('faculty_id', 'MISSING')}")
                print(f"Teacher ID field: {sample.get('teacher_id', 'MISSING')}")
            
            # Count documents with faculty_id
            with_faculty = app.db.feedback.count_documents({'faculty_id': {'$exists': True, '$ne': None, '$ne': ''}})
            without_faculty = app.db.feedback.count_documents({'$or': [
                {'faculty_id': {'$exists': False}},
                {'faculty_id': None},
                {'faculty_id': ''}
            ]})
            
            print(f"\nFeedback documents with faculty_id: {with_faculty}")
            print(f"Feedback documents without faculty_id: {without_faculty}")
            
            # If no faculty_id, try to update from existing data
            if without_faculty > 0:
                print("\nUpdating documents with missing faculty_id...")
                result = app.db.feedback.update_many(
                    {'$or': [
                        {'faculty_id': {'$exists': False}},
                        {'faculty_id': None},
                        {'faculty_id': ''}
                    ]},
                    {'$set': {'faculty_id': 'FAC001'}}  # Default faculty ID
                )
                print(f"Updated {result.modified_count} documents")
            
            # Check users collection for faculty mapping
            users = list(app.db.users.find({}, {'_id': 1, 'faculty_id': 1, 'email': 1}))
            print(f"\nUsers in database: {len(users)}")
            for user in users:
                print(f"  User {user.get('_id')}: faculty_id = {user.get('faculty_id')}")
                
        except Exception as e:
            print(f'❌ Error: {e}')
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    debug_feedback_data()

# Faculty Feedback System - Setup Guide

This guide will walk you through setting up the complete faculty feedback system with React frontend, Flask backend, and MongoDB database.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **Node.js 16+**
- **MongoDB** (local installation or MongoDB Atlas)
- **OpenAI API Key** (for AI analysis features)

## Step 1: Environment Setup

### Backend Environment Variables

1. Navigate to the `backend` directory
2. Copy the example environment file:
   ```bash
   cp env.example .env
   ```
3. Edit `.env` and configure the following:
   ```env
   FLASK_ENV=development
   SECRET_KEY=your-super-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-key-here
   MONGODB_URI=mongodb://localhost:27017/faculty_feedback
   OPENAI_API_KEY=your-openai-api-key-here
   PORT=5000
   ```

### Frontend Environment Variables

1. Navigate to the `frontend` directory
2. Create a `.env` file:
   ```bash
   touch .env
   ```
3. Add the following configuration:
   ```env
   REACT_APP_API_URL=http://localhost:5000/api
   ```

## Step 2: Backend Setup

### Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Database Setup

1. **Local MongoDB:**
   - Install MongoDB locally
   - Start MongoDB service
   - The application will automatically create the database and collections

2. **MongoDB Atlas (Cloud):**
   - Create a MongoDB Atlas account
   - Create a new cluster
   - Get your connection string
   - Update `MONGODB_URI` in your `.env` file

### Create Sample Data (Optional)

You can create sample teachers and feedback data for testing:

```python
# Run this in a Python shell or create a script
from app import create_app
from app.models.feedback import Teacher
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    # Create a sample teacher
    teacher_data = {
        'name': 'Dr. John Smith',
        'email': 'john.smith@university.edu',
        'department': 'Computer Science',
        'subjects': ['Python Programming', 'Data Structures'],
        'password_hash': generate_password_hash('password123')
    }
    
    app.db.teachers.insert_one(teacher_data)
    print("Sample teacher created successfully!")
```

## Step 3: Frontend Setup

### Install Node.js Dependencies

```bash
cd frontend
npm install
```

## Step 4: Running the Application

### Start the Backend Server

```bash
cd backend
python run.py
```

The Flask server will start on `http://localhost:5000`

### Start the Frontend Development Server

```bash
cd frontend
npm start
```

The React app will start on `http://localhost:3000`

## Step 5: Testing the Application

### Login Credentials

Use the sample teacher credentials:
- **Email:** john.smith@university.edu
- **Password:** password123

### Testing Features

1. **Login:** Navigate to the login page and sign in
2. **Dashboard:** View overview metrics and recent feedback
3. **Feedback:** Browse and filter feedback entries
4. **Analytics:** View detailed analytics and charts
5. **AI Analysis:** Test AI-powered feedback analysis

## Step 6: API Testing

### Using Postman or curl

Test the API endpoints:

```bash
# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "john.smith@university.edu", "password": "password123"}'

# Get feedback (requires auth token)
curl -X GET http://localhost:5000/api/feedback \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Step 7: Production Deployment

### Backend Deployment

1. **Environment Variables:**
   - Set `FLASK_ENV=production`
   - Use strong secret keys
   - Configure production MongoDB URI

2. **WSGI Server:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

### Frontend Deployment

1. **Build the application:**
   ```bash
   npm run build
   ```

2. **Deploy to your preferred hosting service:**
   - Netlify
   - Vercel
   - AWS S3 + CloudFront
   - Heroku

## Troubleshooting

### Common Issues

1. **MongoDB Connection Error:**
   - Ensure MongoDB is running
   - Check connection string in `.env`
   - Verify network connectivity

2. **OpenAI API Errors:**
   - Verify API key is correct
   - Check API quota and billing
   - Ensure proper API key permissions

3. **CORS Errors:**
   - Check CORS configuration in `config.py`
   - Verify frontend URL is in allowed origins

4. **JWT Token Issues:**
   - Clear browser localStorage
   - Check token expiration settings
   - Verify JWT secret key

### Logs and Debugging

- **Backend logs:** Check console output when running Flask
- **Frontend logs:** Open browser developer tools
- **Database logs:** Check MongoDB logs

## Security Considerations

1. **Environment Variables:** Never commit `.env` files
2. **API Keys:** Keep OpenAI API key secure
3. **Database:** Use strong passwords and network security
4. **HTTPS:** Use HTTPS in production
5. **Input Validation:** All inputs are validated on both frontend and backend

## Performance Optimization

1. **Database Indexing:** Indexes are automatically created
2. **Caching:** Consider implementing Redis for caching
3. **CDN:** Use CDN for static assets in production
4. **Compression:** Enable gzip compression

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the code comments
3. Check the API documentation in the README
4. Create an issue in the repository

## Next Steps

After successful setup, consider:

1. **Customization:** Modify the UI theme and branding
2. **Additional Features:** Add email notifications, reports export
3. **Integration:** Connect with existing LMS systems
4. **Scaling:** Implement load balancing and database clustering
5. **Monitoring:** Add application monitoring and logging

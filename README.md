# Faculty Feedback System

A comprehensive feedback system for educational institutions that allows students to submit feedback and teachers to view AI-powered analysis and summaries.

## Features

- **Student Feedback Submission**: Students can submit detailed feedback about courses and teachers
- **AI-Powered Analysis**: OpenAI integration for intelligent feedback summarization and analysis
- **Teacher Dashboard**: Comprehensive view of feedback with insights and trends
- **Real-time Updates**: Live feedback monitoring and notifications
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Tech Stack

### Backend
- **Flask**: Python web framework for API development
- **MongoDB**: NoSQL database for storing feedback data
- **OpenAI API**: AI-powered feedback analysis and summarization
- **JWT**: Authentication and authorization

### Frontend
- **React.js**: Modern UI framework
- **Axios**: HTTP client for API communication
- **Material-UI**: Component library for consistent design
- **Chart.js**: Data visualization for feedback analytics

## Project Structure

```
faculty-feedback-system/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── config.py
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── utils/
│   ├── package.json
│   └── README.md
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- MongoDB
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd faculty-feedback-system
   ```

2. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Environment Configuration**
   - Copy `.env.example` to `.env` in both backend and frontend
   - Configure your MongoDB connection string
   - Add your OpenAI API key

5. **Run the Application**
   ```bash
   # Backend (from backend directory)
   python run.py
   
   # Frontend (from frontend directory)
   npm start
   ```

## API Endpoints

### Authentication
- `POST /api/auth/login` - Teacher login
- `POST /api/auth/logout` - Teacher logout

### Feedback
- `GET /api/feedback` - Get all feedback for a teacher
- `GET /api/feedback/<id>` - Get specific feedback
- `POST /api/feedback` - Submit new feedback (student)
- `GET /api/feedback/analytics` - Get feedback analytics

### AI Analysis
- `POST /api/ai/summarize` - Generate AI summary
- `POST /api/ai/analyze` - Perform sentiment analysis

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

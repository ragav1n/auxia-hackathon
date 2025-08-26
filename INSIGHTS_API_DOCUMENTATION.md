# AI Insights API Documentation

## Overview
The AI Insights API provides OpenAI-powered analysis of student feedback data for teachers. This API is designed to work with MongoDB feedback data and generate actionable insights, sentiment analysis, summaries, and teaching recommendations.

## Authentication
All endpoints require JWT authentication. Include the access token in the Authorization header:
```
Authorization: Bearer <access_token>
```

## Base URL
```
http://localhost:5000/api/insights
```

## Endpoints

### 1. Generate Comprehensive Insights
**POST** `/generate`

Analyzes feedback data and provides comprehensive insights including performance analysis, strengths, areas for improvement, and action items.

**Request Body:**
```json
{
  "feedback_data": [
    {
      "content": "Great teacher, very helpful",
      "rating": 5,
      "category": "teaching_quality",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "insights": {
    "analysis": "Detailed AI-generated analysis...",
    "model_used": "gpt-3.5-turbo",
    "tokens_used": 850
  },
  "feedback_count": 25,
  "generated_at": "2024-01-15T15:30:00Z"
}
```

### 2. Analyze Sentiment
**POST** `/analyze-sentiment`

Performs sentiment analysis on feedback data to understand overall student satisfaction.

**Request Body:**
```json
{
  "feedback_data": [
    {
      "content": "The lectures were engaging and informative",
      "rating": 4
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "sentiment_analysis": {
    "sentiment_analysis": "Overall sentiment: Positive (0.75)...",
    "feedback_count": 25
  },
  "analyzed_at": "2024-01-15T15:30:00Z"
}
```

### 3. Summarize Feedback
**POST** `/summarize`

Generates a concise summary of feedback data with key highlights and main concerns.

**Request Body:**
```json
{
  "feedback_data": [
    {
      "content": "Course content is excellent but needs more examples",
      "rating": 4
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "summary": {
    "summary": "Executive summary of feedback...",
    "feedback_count": 25
  },
  "feedback_count": 25,
  "summarized_at": "2024-01-15T15:30:00Z"
}
```

### 4. Generate Teaching Recommendations
**POST** `/recommendations`

Provides specific, actionable teaching recommendations based on feedback analysis.

**Request Body:**
```json
{
  "feedback_data": [
    {
      "content": "More interactive sessions would be helpful",
      "rating": 3
    }
  ],
  "teacher_info": {
    "name": "Dr. Smith",
    "department": "Computer Science",
    "subjects": ["Programming", "Database Systems"]
  }
}
```

**Response:**
```json
{
  "success": true,
  "recommendations": {
    "recommendations": "Specific teaching recommendations...",
    "teacher_info": {
      "name": "Dr. Smith",
      "department": "Computer Science"
    },
    "feedback_count": 25
  },
  "generated_at": "2024-01-15T15:30:00Z"
}
```

## Frontend Integration

### Using the Insights Service

```javascript
import { insightsService } from '../services/insightsService';

// For your team member handling MongoDB integration
const mongoFeedbackData = [
  {
    content: "Great teaching style",
    rating: 5,
    student_id: "STU001",
    course_id: "CS101",
    created_at: "2024-01-15T10:30:00Z"
  }
];

const teacherInfo = {
  name: "Dr. Smith",
  department: "Computer Science",
  subjects: ["Programming", "Database"]
};

// Process MongoDB feedback and get all insights
const results = await insightsService.processMongoFeedback(
  mongoFeedbackData, 
  teacherInfo
);

console.log(results.data.insights);
console.log(results.data.sentiment);
console.log(results.data.summary);
console.log(results.data.recommendations);
```

### Individual API Calls

```javascript
// Generate insights only
const insights = await insightsService.generateInsights(feedbackData);

// Analyze sentiment only
const sentiment = await insightsService.analyzeSentiment(feedbackData);

// Generate summary only
const summary = await insightsService.summarizeFeedback(feedbackData);

// Generate recommendations only
const recommendations = await insightsService.generateRecommendations(
  feedbackData, 
  teacherInfo
);
```

## Data Format Requirements

### Feedback Data Structure
Each feedback object should contain:
- `content` (string): The feedback text
- `rating` (number): Rating from 1-5
- `category` (string, optional): Feedback category
- `created_at` (string, optional): ISO date string
- `student_id` (string, optional): Student identifier
- `course_id` (string, optional): Course identifier

### Teacher Info Structure
- `name` (string): Teacher's full name
- `department` (string): Academic department
- `subjects` (array): List of subjects taught

## Error Handling

All endpoints return consistent error responses:

```json
{
  "success": false,
  "message": "Error description",
  "error": "Detailed error information"
}
```

Common error codes:
- `400`: Bad Request - Invalid or missing feedback data
- `401`: Unauthorized - Invalid or missing JWT token
- `500`: Internal Server Error - OpenAI API error or server issue

## Integration Notes for Team Member

1. **Data Source**: Your MongoDB feedback data can be in any format - the `formatFeedbackForAI()` method will standardize it.

2. **Main Integration Point**: Use `insightsService.processMongoFeedback(mongoData, teacherInfo)` for complete analysis.

3. **Batch Processing**: The API can handle large amounts of feedback data efficiently.

4. **Authentication**: Ensure the teacher is logged in before calling these endpoints.

5. **Error Handling**: Always check the `success` field in responses and handle errors appropriately.

## Example Complete Integration

```javascript
// Your team member's code
async function analyzeTeacherFeedback(teacherId) {
  try {
    // 1. Fetch feedback from MongoDB
    const mongoFeedback = await fetchFeedbackFromMongo(teacherId);
    
    // 2. Get teacher information
    const teacherInfo = await getTeacherInfo(teacherId);
    
    // 3. Process with AI insights
    const analysis = await insightsService.processMongoFeedback(
      mongoFeedback, 
      teacherInfo
    );
    
    if (analysis.success) {
      // 4. Display results to teacher
      displayInsights(analysis.data);
    } else {
      console.error('Analysis failed:', analysis.error);
    }
  } catch (error) {
    console.error('Integration error:', error);
  }
}
```

This API provides a complete solution for AI-powered feedback analysis that integrates seamlessly with your MongoDB data source.

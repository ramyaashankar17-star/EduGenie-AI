# PHASE 3 – PROJECT DESIGN
## Project Name: EduGenie AI – Google Gemini Powered Learning Assistant

### 1. System Architecture
The system follows a web-based client-server architecture.

Student
↓
HTML/CSS Web Interface
↓
FastAPI Backend
↓
Selected Learning Module
↓
Google Gemini API
↓
Generated Educational Response
↓
Web Interface
↓
Student

### 2. Main Modules
#### Q&A Module
Accepts an academic question and generates an appropriate answer.

#### Explanation Module
Explains a topic in simple and readable language.

#### Quiz Module
Generates multiple-choice questions from a topic or passage.

#### Summary Module
Converts lengthy educational content into a concise summary.

#### Learning Path Module
Generates a structured learning path from beginner to advanced level.

### 3. API Endpoints
- /qa
- /explain
- /quiz
- /summarize
- /learn/recommendations

### 4. User Flow
1. User opens EduGenie AI.
2. User selects a task.
3. User enters the required content.
4. Frontend sends the request to the FastAPI backend.
5. The selected module processes the request.
6. The Gemini model generates the response.
7. The response is displayed to the user.

### 5. Folder/Module Design
- main.py – FastAPI application
- gemini_client.py – Gemini API communication
- explanation_module.py – Concept explanation
- qna.py – Question answering
- quiz_module.py – Quiz generation
- summary_module.py – Summarization
- learning_path.py – Learning recommendations
- templates/ – HTML frontend
- static/ – CSS and frontend styling

### 6. Phase Conclusion
The system architecture, user flow, modules, API endpoints, and application structure were designed before implementation.

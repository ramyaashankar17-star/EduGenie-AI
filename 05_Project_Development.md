# PHASE 5 – PROJECT DEVELOPMENT
## Project Name: EduGenie AI – Google Gemini Powered Learning Assistant

### 1. Development Overview
EduGenie AI was developed as a lightweight web-based educational assistant. FastAPI is used for the backend, HTML/CSS for the frontend, and Google Gemini is used for generative AI capabilities.

### 2. Backend Development
The FastAPI backend provides endpoints for the major learning functions:
- /qa
- /explain
- /quiz
- /summarize
- /learn/recommendations

### 3. AI Module Development
#### Q&A
Provides answers to educational questions using generative AI.

#### Explanation
Provides simplified explanations of difficult concepts.

#### Quiz
Generates multiple-choice questions for learning and revision.

#### Summary
Summarizes lengthy educational passages while retaining important information.

#### Learning Path
Provides structured beginner-to-advanced learning recommendations and resources.

### 4. Frontend Development
The web interface contains:
- Task selection
- Text input area
- Submit button
- Result display area
- Responsive styling

### 5. Project Structure
- main.py
- gemini_client.py
- explanation_module.py
- qna.py
- quiz_module.py
- summary_module.py
- learning_path.py
- templates/index.html
- static/style.css
- requirements.txt

### 6. Local Execution
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
The application can be accessed locally through the configured browser address.

### 7. Security
The Gemini API key must be stored securely as an environment variable. It must never be committed to the public repository.

### 8. Phase Conclusion
The EduGenie AI backend, AI modules, frontend interface, and integration flow were developed into a working educational assistant.

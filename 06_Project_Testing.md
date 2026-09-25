# PHASE 6 – PROJECT TESTING
## Project Name: EduGenie AI – Google Gemini Powered Learning Assistant

### 1. Testing Objective
The objective of testing is to verify that EduGenie AI accepts valid input, invokes the correct learning function, handles common errors, and displays the generated response correctly.

### 2. Functional Test Cases
| Test ID | Test Case | Expected Result | Status |
|---|---|---|---|
| TC01 | Open application | Home page loads | Pass |
| TC02 | Ask an academic question | AI answer is displayed | Pass |
| TC03 | Request concept explanation | Simplified explanation is displayed | Pass |
| TC04 | Generate quiz | Quiz questions are displayed | Pass |
| TC05 | Summarize text | Concise summary is displayed | Pass |
| TC06 | Request learning path | Structured learning path is displayed | Pass |
| TC07 | Submit empty input | Validation/error message is displayed | Pass |
| TC08 | API/model failure | User-friendly error is handled | Pass |

### 3. Integration Testing
The complete flow was checked:
Frontend → FastAPI → Selected Module → Gemini API → Response → Frontend.

### 4. Error Handling
The system should handle:
- Empty input
- Invalid requests
- API failures
- Invalid model responses
- Quiz JSON parsing errors

### 5. Test Evidence
Actual screenshots of the working tests can be added to this phase folder:
- Q&A screenshot
- Explanation screenshot
- Quiz screenshot
- Summary screenshot
- Learning Path screenshot
- Error/validation screenshot

### 6. Phase Conclusion
The major EduGenie AI functions and their integration flow were tested using functional and integration test cases.

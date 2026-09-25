from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


app = FastAPI(title="EduGenie AI")


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/qa")
async def qa(request: Request):
    data = await request.json()
    question = data.get("text", "").strip()

    if not question:
        return {"result": "Please enter a question."}

    return {"result": answer_question(question)}


@app.post("/explain")
async def explain(request: Request):
    data = await request.json()
    topic = data.get("text", "").strip()

    if not topic:
        return {"result": "Please enter a topic."}

    return {"result": explain_topic(topic)}


@app.post("/quiz")
async def quiz(request: Request):
    data = await request.json()
    topic = data.get("text", "").strip()

    if not topic:
        return {"result": "Please enter a topic."}

    return {"result": generate_quiz(topic)}


@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "").strip()

    if not text:
        return {"result": "Please enter some text."}

    return {"result": summarize_text(text)}


@app.post("/learn/recommendations")
async def recommendations(request: Request):
    data = await request.json()
    topic = data.get("text", "").strip()

    if not topic:
        return {"result": "Please enter a topic."}

    return {"result": get_learning_recommendations(topic)}
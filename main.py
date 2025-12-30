from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
def chat(req: ChatRequest):
    msg = req.message.lower()

    if "hello" in msg or "hi" in msg:
        reply = "Hello! 😊"
    elif "how are you" in msg:
        reply = "I am fine! How can I help you?"
    elif "bye" in msg:
        reply = "Goodbye 👋"
    else:
        reply = "Sorry, I didn't understand."

    return {"reply": reply}

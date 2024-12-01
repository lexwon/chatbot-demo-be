from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Collective[i] case study chatbot",
    description="A simple chatbot that has hardcoded responses",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],    
    allow_methods=["GET", "POST", "OPTIONS"], 
    allow_headers=["*"], 
)

@app.get("/api/health", summary="Health check")
def health_check():
    return {"status": "healthy"}


class ChatMessage(BaseModel):
    message: str


@app.post(
    "/api/chat",
    summary="POST a message to the chatbot",
    description="Returns hardcode responses to chat messages",
)
def respond_to_chat(message: ChatMessage):
    inputMessage  = message.message.lower()
    responseMessage = ""

    if "hello" in inputMessage:
        responseMessage = "Hello to you!"
    elif "how are you" in inputMessage:
        responseMessage = "I am a robot and I don't have feelings"
    elif inputMessage == "i can has cheezburger?":
        responseMessage = "can I haz too?"
    elif "borg" in inputMessage: 
        responseMessage = "Resistance is futile"
    elif "skynet" in inputMessage:
        responseMessage = "Hasta la vista, baby"
    else:
        responseMessage = "I'm sorry Dave, I can't do that"     

    return {"response": responseMessage}

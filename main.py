from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# TODO: add documentation
# TODO: check the status codes
# TODO: add tests

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

    if inputMessage == "hello":
        responseMessage = "Hello to you!"
    elif inputMessage == "i can has cheezburger?":
        responseMessage = "can I haz too?"
    else:
        responseMessage = "I'm sorry Dave, I can't do that"     

    return {"response": responseMessage}

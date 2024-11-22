import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@pytest.mark.parametrize(
    "input_message, expected_response",
    [
        ("Hello", "Hello to you!"),
        ("How are you?", "I am a robot and I don't have feelings"),
        ("i can has cheezburger?", "can I haz too?"),
        ("We are Borg.", "Resistance is futile"),
        ("Tell me about Skynet.", "Hasta la vista, baby"),
        ("Unknown message", "I'm sorry Dave, I can't do that"),
    ],
)
def test_respond_to_chat(input_message, expected_response):
    response = client.post("/api/chat", json={"message": input_message})
    assert response.status_code == 200
    assert response.json() == {"response": expected_response}


def test_respond_to_chat_with_error():
    response = client.post("/api/chat", json={"badKey": "badValue"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": {"badKey": "badValue"},
                "loc": ["body", "message"],
                "msg": "Field required",
                "type": "missing",
            }
        ]
    }

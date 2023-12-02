from fastapi.testclient import TestClient
from PW5.main import app

ENG_TXT = "This is a test message in English this test will test whether the application can generate a summary. If the " \
          "text is short, the application will return it as a summary"

client = TestClient(app)


def test_get_base_page():
    response = client.get("/summary_text/")
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["message"] == "Welcome to Base Page"

def test_post_eng_text():
    response = client.post("/summary_text/", json={"text": ENG_TXT})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['Краткое содержание:'] == "This is a test message in English."


def test_post_rus_text():
    response = client.post("/summary_text/", json={"text": "Тестовая строка"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['Краткое содержание:'] == "Тестируете свой тест на домашнюю работу?"

def test_post_empty_string():
    response = client.post("/summary_text/", json={"text": ""})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['Краткое содержание:'] == "BainAD, talan Deput-General"

def test_error_empty_json():
    response = client.post("/summary_text/", json={})
    json_data = response.json()
    assert response.status_code == 422
    assert json_data['detail'][0]['type'] == "missing"
    assert json_data['detail'][0]['loc'] == ["body", "text"]
    assert json_data['detail'][0]['msg'] == "Field required"

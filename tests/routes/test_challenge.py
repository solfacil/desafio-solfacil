from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_vowel_count():
    response = client.post(
        "/soupilar/vowel_count",
        json={"words": ["hello", "world", "fastapi"]},
    )

    assert response.status_code == 200
    assert response.json() == {"hello": 2, "world": 1, "fastapi": 3}


def test_sort_words_asc():
    response = client.post(
        "/soupilar/sort",
        json={"words": ["banana", "apple", "cherry"], "order": "asc"},
    )

    assert response.status_code == 200
    assert response.json() == ["apple", "banana", "cherry"]


def test_sort_words_desc():
    response = client.post(
        "/soupilar/sort",
        json={"words": ["banana", "apple", "cherry"], "order": "desc"},
    )

    assert response.status_code == 200
    assert response.json() == ["cherry", "banana", "apple"]

import sys
sys.path = ['', '..'] + sys.path[1:]

import requests
from fastapi import status
from fastapi.testclient import TestClient

from src.api import app

client: requests.Session = TestClient(app)

date = {
    "questions_num": 1
}

def test_user():
    response = client.post('/v1/users', json=date)
    assert response.status_code == status.HTTP_201_CREATED

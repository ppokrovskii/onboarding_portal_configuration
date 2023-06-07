from unittest import TestCase

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestHome(TestCase):
    def test_home(self):
        result = client.get("/")
        self.assertEqual(200, result.status_code)
        self.assertEqual("http://localhost:8000/docs", result.text)
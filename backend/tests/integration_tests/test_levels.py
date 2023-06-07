from unittest import TestCase

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestLevels(TestCase):
    def test_create_level(self):
        level = {
            "name": "1"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        # drop None values
        result_json = {k: v for k, v in result.json().items() if v is not None}
        self.assertEqual(result_json, level)

    def test_create_level_with_parent(self):
        parent = {
            "name": "parent"
        }
        result = client.post("/api/levels", json=parent)
        self.assertEqual(201, result.status_code)
        self.assertEqual(parent, result.json())
        level = {
            "name": "level",
            "parent": "parent"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        self.assertEqual(level, result.json())

    def test_create_level_with_parent_not_found(self):
        level = {
            "name": "level",
            "parent": "parent"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(404, result.status_code)
        self.assertEqual("Parent Level parent not found", result.json()["detail"])

    def test_level_already_exists(self):
        level = {
            "name": "1"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        result = client.post("/api/levels", json=level)
        self.assertEqual(400, result.status_code)
        self.assertEqual("Level 1 already exists", result.json()["detail"])

    def test_get_levels(self):
        result = client.get("/api/levels")
        self.assertEqual(200, result.status_code)
        self.assertEqual([], result.json())

    def test_get_level_by_name_not_found(self):
        result = client.get("/api/levels/name/1")
        self.assertEqual(404, result.status_code)
        self.assertEqual("level 1 not found", result.json()["detail"])

    def test_get_level_by_name(self):
        level = {
            "name": "1"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        result = client.get("/api/levels/name/1")
        self.assertEqual(200, result.status_code)
        self.assertEqual(level, result.json())
from unittest import TestCase

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestFeatures(TestCase):
    def test_create_feature(self):
        feature = {
            "name": "1"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        self.assertEqual(feature, result.json())

    def test_create_feature_with_parent(self):
        parent = {
            "name": "parent"
        }
        result = client.post("/api/features", json=parent)
        self.assertEqual(201, result.status_code)
        self.assertEqual(parent, result.json())
        feature = {
            "name": "feature",
            "parent": "parent"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        self.assertEqual(feature, result.json())

    def test_create_feature_with_parent_not_found(self):
        feature = {
            "name": "feature",
            "parent": "parent"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(404, result.status_code)
        self.assertEqual("Parent Feature parent not found", result.json()["detail"])

    def test_feature_already_exists(self):
        feature = {
            "name": "1"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        result = client.post("/api/features", json=feature)
        self.assertEqual(400, result.status_code)
        self.assertEqual("Feature 1 already exists", result.json()["detail"])

    def test_get_features(self):
        result = client.get("/api/features")
        self.assertEqual(200, result.status_code)
        self.assertEqual([], result.json())

    def test_get_feature_by_name_not_found(self):
        result = client.get("/api/features/name/1")
        self.assertEqual(404, result.status_code)
        self.assertEqual("Feature 1 not found", result.json()["detail"])

    def test_get_feature_by_name(self):
        feature = {
            "name": "1"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        result = client.get("/api/features/name/1")
        self.assertEqual(200, result.status_code)
        self.assertEqual(feature, result.json())

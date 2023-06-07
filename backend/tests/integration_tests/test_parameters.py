from unittest import TestCase

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestParameters(TestCase):
    def test_create_parameter(self):
        # create level
        level = {
            "name": "Tenant"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), level)
        # create feature
        feature = {
            "name": "Basic Details"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), feature)
        # create parameter
        parameter = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": "Tenant",
            "features": [
                "Basic Details",
            ]
        }
        expected_response = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": {
                "name": "Tenant",
            },
            "features": [
                {
                    "name": "Basic Details",
                }
            ]
        }
        result = client.post("/api/parameters", json=parameter)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), expected_response)

    def test_create_parameter_with_level_not_found(self):
        # create feature
        feature = {
            "name": "Basic Details"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), feature)
        # create parameter
        parameter = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": "Tenant",
            "features": [
                "Basic Details",
            ]
        }
        result = client.post("/api/parameters", json=parameter)
        self.assertEqual(404, result.status_code)
        self.assertEqual({"detail": "Level with name Tenant doesnt exist"}, result.json())

    def test_create_parameter_with_feature_not_found(self):
        # create level
        level = {
            "name": "Tenant"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), level)
        # create parameter
        parameter = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": "Tenant",
            "features": [
                "Basic Details",
            ]
        }
        result = client.post("/api/parameters", json=parameter)
        self.assertEqual(404, result.status_code)
        self.assertEqual({"detail": "Feature with name Basic Details doesnt exist"}, result.json())

    def test_create_parameter_exising_name(self):
        # create level
        level = {
            "name": "Tenant"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), level)
        # create feature
        feature = {
            "name": "Basic Details"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), feature)
        # create parameter
        parameter = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": "Tenant",
            "features": [
                "Basic Details",
            ]
        }
        expected_response = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": {
                "name": "Tenant",
            },
            "features": [
                {
                    "name": "Basic Details",
                }
            ]
        }
        result = client.post("/api/parameters", json=parameter)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), expected_response)
        # create parameter with same name
        result = client.post("/api/parameters", json=parameter)
        self.assertEqual(400, result.status_code)
        self.assertEqual({"detail": "Parameter with name Financial Institution - Name already exists"}, result.json())

    def test_create_parameter_existing_col_code(self):
        # create level
        level = {
            "name": "Tenant"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), level)
        # create feature
        feature = {
            "name": "Basic Details"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), feature)
        # create parameter
        parameter = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": "Tenant",
            "features": [
                "Basic Details",
            ]
        }
        expected_response = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": {
                "name": "Tenant",
            },
            "features": [
                {
                    "name": "Basic Details",
                }
            ]
        }
        result = client.post("/api/parameters", json=parameter)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), expected_response)
        # create parameter with same col_code
        parameter = {
            "name": "Financial Institution - Name 2",
            "col_code": "nic-fi-name",
            "level": "Tenant",
            "features": [
                "Basic Details",
            ]
        }
        result = client.post("/api/parameters", json=parameter)
        self.assertEqual(400, result.status_code)
        self.assertEqual({"detail": "Parameter with col_code nic-fi-name already exists"}, result.json())


class TestGetParameter(TestCase):
    def test_get_parameter(self):
        # create level
        level = {
            "name": "Tenant"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), level)
        # create feature
        feature = {
            "name": "Basic Details"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), feature)
        # create parameter
        parameter = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": "Tenant",
            "features": [
                "Basic Details",
            ]
        }
        expected_response = {
            "name": "Financial Institution - Name",
            "col_code": "nic-fi-name",
            "level": {
                "name": "Tenant",
            },
            "features": [
                {
                    "name": "Basic Details",
                }
            ]
        }
        result = client.post("/api/parameters", json=parameter)
        self.assertEqual(201, result.status_code)
        self.assertEqual(expected_response, result.json())
        # get parameter
        result = client.get("/api/parameters/name/Financial Institution - Name")
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_response, result.json())

    def test_get_parameter_not_found(self):
        # get parameter
        result = client.get("/api/parameters/name/Financial Institution - Name")
        self.assertEqual(404, result.status_code)
        self.assertEqual({"detail": "Parameter with name Financial Institution - Name not found"}, result.json())


    def test_get_parameters(self):
        # create level
        level = {
            "name": "Tenant"
        }
        result = client.post("/api/levels", json=level)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), level)
        # create feature
        feature = {
            "name": "Basic Details"
        }
        result = client.post("/api/features", json=feature)
        self.assertEqual(201, result.status_code)
        self.assertEqual(result.json(), feature)
        # create parameters
        parameters = [
            {
                "name": "Financial Institution - Name",
                "col_code": "nic-fi-name",
                "level": "Tenant",
                "features": [
                    "Basic Details",
                ]
            },
            {
                "name": "Financial Institution - Type",
                "col_code": "nic-fi-type",
                "level": "Tenant",
                "features": [
                    "Basic Details",
                ]
            }
        ]
        expected_response = [
            {
                "name": "Financial Institution - Name",
                "col_code": "nic-fi-name",
                "level": {
                    "name": "Tenant",
                },
                "features": [
                    {
                        "name": "Basic Details",
                    }
                ]
            },
            {
                "name": "Financial Institution - Type",
                "col_code": "nic-fi-type",
                "level": {
                    "name": "Tenant",
                },
                "features": [
                    {
                        "name": "Basic Details",
                    }
                ]
            }
        ]
        result = client.post("/api/parameters", json=parameters[0])
        self.assertEqual(201, result.status_code)
        self.assertEqual(expected_response[0], result.json())
        result = client.post("/api/parameters", json=parameters[1])
        self.assertEqual(201, result.status_code)
        self.assertEqual(expected_response[1], result.json())
        # get parameters
        result = client.get("/api/parameters")
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_response, result.json())

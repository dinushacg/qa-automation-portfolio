"""
API tests for https://reqres.in — a free public REST API
used as the test target for this portfolio project.
"""
import pytest
import requests
import jsonschema

BASE_URL = "https://reqres.in/api"

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "email", "first_name", "last_name", "avatar"],
    "properties": {
        "id":         {"type": "integer"},
        "email":      {"type": "string"},
        "first_name": {"type": "string"},
        "last_name":  {"type": "string"},
        "avatar":     {"type": "string"},
    }
}

class TestGetUsers:

    def test_get_users_returns_200(self):
        resp = requests.get(f"{BASE_URL}/users?page=1")
        assert resp.status_code == 200

    def test_get_users_returns_json(self):
        resp = requests.get(f"{BASE_URL}/users?page=1")
        assert resp.headers["Content-Type"].startswith("application/json")

    def test_get_users_data_is_list(self):
        resp = requests.get(f"{BASE_URL}/users?page=1")
        assert isinstance(resp.json()["data"], list)

    def test_each_user_matches_schema(self):
        resp = requests.get(f"{BASE_URL}/users?page=1")
        for user in resp.json()["data"]:
            jsonschema.validate(instance=user, schema=USER_SCHEMA)

    def test_get_single_user_returns_200(self):
        resp = requests.get(f"{BASE_URL}/users/2")
        assert resp.status_code == 200

    def test_get_nonexistent_user_returns_404(self):
        resp = requests.get(f"{BASE_URL}/users/999")
        assert resp.status_code == 404

    def test_single_user_schema_valid(self):
        resp = requests.get(f"{BASE_URL}/users/2")
        user = resp.json()["data"]
        jsonschema.validate(instance=user, schema=USER_SCHEMA)


class TestCreateUser:

    def test_create_user_returns_201(self):
        payload = {"name": "Dinusha", "job": "QA Engineer"}
        resp = requests.post(f"{BASE_URL}/users", json=payload)
        assert resp.status_code == 201

    def test_create_user_response_has_id(self):
        payload = {"name": "Dinusha", "job": "QA Engineer"}
        resp = requests.post(f"{BASE_URL}/users", json=payload)
        assert "id" in resp.json()

    def test_create_user_name_matches(self):
        payload = {"name": "Dinusha", "job": "QA Engineer"}
        resp = requests.post(f"{BASE_URL}/users", json=payload)
        assert resp.json()["name"] == "Dinusha"


class TestUpdateUser:

    def test_update_user_returns_200(self):
        payload = {"name": "Dinusha", "job": "Senior QA Engineer"}
        resp = requests.put(f"{BASE_URL}/users/2", json=payload)
        assert resp.status_code == 200

    def test_update_user_job_reflects_change(self):
        payload = {"name": "Dinusha", "job": "Senior QA Engineer"}
        resp = requests.put(f"{BASE_URL}/users/2", json=payload)
        assert resp.json()["job"] == "Senior QA Engineer"


class TestDeleteUser:

    def test_delete_user_returns_204(self):
        resp = requests.delete(f"{BASE_URL}/users/2")
        assert resp.status_code == 204
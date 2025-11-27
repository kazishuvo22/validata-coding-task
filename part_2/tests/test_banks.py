import pytest
import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from models.bank_model import db, Bank

@pytest.fixture
def client():
    app = create_app()
    app.config.from_object("configs.test_config.TestConfig")

    with app.app_context():
        db.create_all()  # Create tables in memory
        yield app.test_client()
        db.drop_all()

# Helper to create a bank in tests
def create_bank(client, name="Test Bank", location="Test Location"):
    return client.post(
        "/api/banks",
        data=json.dumps({"name": name, "location": location}),
        content_type="application/json"
    )

# Test CRUD operations

def test_create_bank(client):
    response = create_bank(client)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "Test Bank"
    assert data["location"] == "Test Location"

def test_get_all_banks(client):
    create_bank(client, "Bank 1", "Loc 1")
    create_bank(client, "Bank 2", "Loc 2")

    response = client.get("/api/banks")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]["name"] == "Bank 1"

def test_get_single_bank(client):
    res = create_bank(client, "Single Bank", "Single Loc")
    bank_id = json.loads(res.data)["id"]

    response = client.get(f"/api/banks/{bank_id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "Single Bank"

def test_update_bank(client):
    res = create_bank(client)
    bank_id = json.loads(res.data)["id"]

    response = client.put(
        f"/api/banks/{bank_id}",
        data=json.dumps({"name": "Updated Bank", "location": "Updated Loc"}),
        content_type="application/json"
    )

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "Updated Bank"

def test_delete_bank(client):
    res = create_bank(client)
    bank_id = json.loads(res.data)["id"]

    response = client.delete(f"/api/banks/{bank_id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] is True

    # Confirm deletion
    get_response = client.get(f"/api/banks/{bank_id}")
    assert get_response.status_code == 404
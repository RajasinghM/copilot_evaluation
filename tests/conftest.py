import pytest
from fastapi.testclient import TestClient
from src.app import app, activities
import copy

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: Save original state
    original = copy.deepcopy(activities)
    yield
    # Assert: Restore after test
    activities.clear()
    activities.update(copy.deepcopy(original))

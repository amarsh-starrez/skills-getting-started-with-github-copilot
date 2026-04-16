from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Provide a FastAPI test client."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities so each test starts from a known state."""
    original_data = deepcopy(activities)

    yield

    activities.clear()
    activities.update(deepcopy(original_data))

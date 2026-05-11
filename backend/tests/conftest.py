from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def mock_db_session():
    db = MagicMock()
    db.query.return_value.filter.return_value.first.return_value = None
    db.query.return_value.filter.return_value.all.return_value = []
    return db


@pytest.fixture(scope="function")
def client_mock(mock_db_session):
    def override_get_db():
        try:
            yield mock_db_session
        finally:
            pass

    with patch('backend.main.engine'):
        with patch('backend.models.SessionLocal', return_value=mock_db_session):
            from backend.main import app
            from backend.models import get_db

            app.dependency_overrides[get_db] = override_get_db

            with TestClient(app) as c:
                yield c

            app.dependency_overrides.clear()

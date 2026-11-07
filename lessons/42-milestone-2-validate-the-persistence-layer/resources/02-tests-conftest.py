import pytest


@pytest.fixture
def db_path(tmp_path):
    path = tmp_path / 'expenses.sqlite3'
    yield path
    path.unlink(missing_ok=True)

import os
from pathlib import Path

import pytest

from src.database import Base, engine


# delete db after all tests
@pytest.fixture(scope="function", autouse=True)
def cleanup():
    # recreate all tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    print("cleaning up")
    # db_file = Path(__file__).parent.parent / "integration_tests.db"
    # db_file.unlink(missing_ok=True)

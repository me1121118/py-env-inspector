import pytest
from py_env_inspector import audit_env, parse_env_file

def test_parse_env_file():
    content = """
    # Database configuration
    DATABASE_URL=postgres://...
    REDIS_URL=redis://...
    PORT=8000
    """
    keys = parse_env_file(content)
    assert keys == {"DATABASE_URL", "REDIS_URL", "PORT"}

def test_audit_env():
    template = """
    DB_HOST=
    DB_USER=
    SECRET_KEY=
    """
    active_env = {
        "DB_HOST": "localhost",
        "DB_USER": "",          # Empty!
        # SECRET_KEY is missing!
    }

    report = audit_env(example_content=template, target_env=active_env)
    assert report.is_valid is False
    assert report.missing_keys == {"SECRET_KEY"}
    assert report.empty_keys == {"DB_USER"}

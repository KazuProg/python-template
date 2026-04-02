"""Smoke tests for my_project."""

from my_project import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"

import pytest
from src.library import validate_isbn

def test_validate_isbn_valid_13_digits():
    assert validate_isbn("9780134685991") is True

def test_validate_isbn_empty_string_raises():
    with pytest.raises(ValueError):
        validate_isbn("")

def test_validate_isbn_too_short_raises():
    with pytest.raises(ValueError):
        validate_isbn("12345")

def test_validate_isbn_letters_symbols_raises():
    with pytest.raises(ValueError):
        validate_isbn("abc-not-an-isbn")
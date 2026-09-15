import pytest
from src.library import validate_isbn

@pytest.mark.parametrize("isbn, should_pass", [
    ("1" * 11, False),
    ("1" * 12, False),
    ("1" * 13, True),
    ("1" * 14, False),
    ("1" * 15, False),
])
def test_validate_isbn_length_boundaries(isbn, should_pass):
    if should_pass:
        assert validate_isbn(isbn) is True
    else:
        with pytest.raises(ValueError):
            validate_isbn(isbn)

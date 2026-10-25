import pytest

from src.library import Book


@pytest.fixture
def book_details():
    return ("9780132350884", "Clean Code", "R. Martin", 2)


@pytest.mark.parametrize("isbn", ["abc", "", "978013235088"])
def test_book_rejects_invalid_isbn(book_details, isbn):
    with pytest.raises(ValueError):
        Book(isbn, *book_details[1:])

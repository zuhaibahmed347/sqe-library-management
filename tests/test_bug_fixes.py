import pytest

from src.library import Book, Library


@pytest.fixture
def book_details():
    return ("9780132350884", "Clean Code", "R. Martin")


@pytest.mark.parametrize("copies", [-1, 1.5, "two"])
def test_book_rejects_negative_and_non_integer_copies(book_details, copies):
    with pytest.raises(ValueError):
        Book(*book_details, copies)


@pytest.fixture
def library_with_book():
    library = Library()
    book = Book("9780132350884", "Clean Code", "R. Martin", 2)
    library.add_book(book)
    return library, book


@pytest.mark.parametrize("query", ["clean code", "CLEAN CODE"])
def test_search_by_title_is_case_insensitive(library_with_book, query):
    library, book = library_with_book

    assert library.search_by_title(query) == [book]

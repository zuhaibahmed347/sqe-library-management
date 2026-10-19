import pytest
from src.library import Library, Book


@pytest.fixture(scope="module")
def catalog_data():
    # scope="module": built once per test file. Use it for expensive setup that
    # tests only READ (never modify), like loading data or opening a connection.
    return [
        ("9780132350884", "Clean Code", "R. Martin", 2),
        ("9780135957059", "The Pragmatic Programmer", "D. Thomas", 1),
    ]


@pytest.fixture
def library():
    # scope="function" (the default): a fresh empty Library for every test.
    # Use it for anything tests MUTATE, so tests stay independent of each other.
    return Library()


@pytest.fixture
def populated_library(catalog_data):
    lib = Library()
    for isbn, title, author, copies in catalog_data:
        lib.add_book(Book(isbn, title, author, copies))
    return lib

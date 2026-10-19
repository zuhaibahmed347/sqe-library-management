from src.library import Book


def test_total_available_copies_empty_catalog(library):
    # Arrange: empty library from fixture. Act + Assert:
    assert library.total_available_copies() == 0


def test_total_available_copies_single_book(library):
    library.add_book(Book("9780132350884", "Clean Code", "R. Martin", 2))
    assert library.total_available_copies() == 2


def test_total_available_copies_multiple_books(populated_library):
    assert populated_library.total_available_copies() == 3

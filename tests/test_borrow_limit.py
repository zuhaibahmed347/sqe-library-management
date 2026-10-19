import pytest


def test_borrow_at_four_books_succeeds(library):
    library.borrowed_counts["m1"] = 4
    assert library.borrow_book("m1", "1234567890123") is True


def test_borrow_at_five_books_blocked(library):
    library.borrowed_counts["m1"] = 5
    with pytest.raises(ValueError):
        library.borrow_book("m1", "1234567890123")


def test_borrow_at_six_books_blocked(library):
    library.borrowed_counts["m1"] = 6
    with pytest.raises(ValueError):
        library.borrow_book("m1", "1234567890123")

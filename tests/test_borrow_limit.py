import pytest
from src.library import Library

def test_borrow_at_four_books_succeeds():
    lib = Library()
    lib.borrowed_counts["m1"] = 4
    assert lib.borrow_book("m1", "1234567890123") is True

def test_borrow_at_five_books_blocked():
    lib = Library()
    lib.borrowed_counts["m1"] = 5
    with pytest.raises(ValueError):
        lib.borrow_book("m1", "1234567890123")

def test_borrow_at_six_books_blocked():
    lib = Library()
    lib.borrowed_counts["m1"] = 6
    with pytest.raises(ValueError):
        lib.borrow_book("m1", "1234567890123")

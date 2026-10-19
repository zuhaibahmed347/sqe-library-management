import pytest


@pytest.mark.parametrize(
    "already_borrowed, should_succeed",
    [
        (0, True),
        (1, True),
        (4, True),
        (5, False),
        (6, False),
        (10, False),
    ],
    ids=[
        "zero-books-allowed",
        "one-book-allowed",
        "four-books-last-slot-allowed",
        "five-books-at-limit-blocked",
        "six-books-over-limit-blocked",
        "ten-books-far-over-limit-blocked",
    ],
)
def test_borrow_book_limit(library, already_borrowed, should_succeed):
    library.borrowed_counts["m1"] = already_borrowed

    if should_succeed:
        assert library.borrow_book("m1", "1234567890123") is True
        assert library.borrowed_counts["m1"] == already_borrowed + 1
    else:
        with pytest.raises(ValueError):
            library.borrow_book("m1", "1234567890123")
        assert library.borrowed_counts["m1"] == already_borrowed

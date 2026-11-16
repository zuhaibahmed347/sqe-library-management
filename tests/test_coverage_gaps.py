import pytest

from src.library import Book, Library, Member, validate_isbn


def test_add_book_rejects_duplicate_isbn(library):
    book = Book("9780132350884", "Clean Code", "R. Martin", 2)
    library.add_book(book)

    with pytest.raises(ValueError, match="already exists"):
        library.add_book(Book(book.isbn, "Another title", "Another author", 1))


def test_get_most_popular_book_returns_none_for_empty_counts(library):
    assert library.get_most_popular_book({}) is None


def test_get_most_popular_book_returns_isbn_with_highest_count(library):
    counts = {"9780132350884": 2, "9780135957059": 5}

    assert library.get_most_popular_book(counts) == "9780135957059"


@pytest.mark.parametrize(
    "days_late, expected",
    [(-1, 0.0), (3, 1.5)],
)
def test_calculate_fine_handles_negative_and_positive_days(library, days_late, expected):
    assert library.calculate_fine(days_late) == expected


def test_member_stores_identity_and_name():
    member = Member("m1", "Ada Lovelace")

    assert member.member_id == "m1"
    assert member.name == "Ada Lovelace"


def test_validate_isbn_rejects_non_string_values():
    with pytest.raises(ValueError, match="must be a string"):
        validate_isbn(9780132350884)

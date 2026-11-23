import pytest

from src.library import Library, Member, borrow_percentile


def test_borrow_percentile_places_top_borrower_at_100_percent():
    library = Library()
    for member_id in ("m1", "m2", "m3"):
        library.members[member_id] = Member(member_id, member_id)

    library.borrowed_counts.update({"m1": 1, "m2": 3, "m3": 5})

    assert borrow_percentile("m3", library) == 100.0


def test_borrow_percentile_low_borrower_is_not_top():
    library = Library()
    for member_id in ("m1", "m2", "m3"):
        library.members[member_id] = Member(member_id, member_id)

    library.borrowed_counts.update({"m1": 1, "m2": 3, "m3": 5})

    assert borrow_percentile("m1", library) == 0.0

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


def test_borrow_percentile_accepts_member_object():
    library = Library()
    for member_id in ("m1", "m2", "m3"):
        library.members[member_id] = Member(member_id, member_id)
    library.borrowed_counts.update({"m1": 1, "m2": 3, "m3": 5})

    assert borrow_percentile(library.members["m2"], library) == 50.0


def test_borrow_percentile_single_member_is_top():
    library = Library()
    library.members["m1"] = Member("m1", "One")

    assert borrow_percentile("m1", library) == 100.0


def test_borrow_percentile_empty_library_raises():
    with pytest.raises(ValueError, match="no registered members"):
        borrow_percentile("m1", Library())


def test_borrow_percentile_unknown_member_raises():
    library = Library()
    library.members["m1"] = Member("m1", "One")

    with pytest.raises(ValueError, match="Member not found"):
        borrow_percentile("missing", library)


def test_borrow_percentile_invalid_member_type_raises():
    library = Library()
    library.members["m1"] = Member("m1", "One")

    with pytest.raises(ValueError, match="member ID"):
        borrow_percentile(123, library)


def test_borrow_percentile_members_with_no_count_are_zero():
    library = Library()
    for member_id in ("m1", "m2", "m3"):
        library.members[member_id] = Member(member_id, member_id)
    library.borrowed_counts["m3"] = 2

    assert borrow_percentile("m1", library) == 0.0


def test_borrow_percentile_equal_scores_rank_against_lower_scores():
    library = Library()
    for member_id in ("m1", "m2", "m3"):
        library.members[member_id] = Member(member_id, member_id)
    library.borrowed_counts.update({"m1": 1, "m2": 3, "m3": 3})

    assert borrow_percentile("m2", library) == 50.0

import pytest
from src.library import Library

@pytest.mark.parametrize('starting_count,should_succeed', [
    (3, True),   # valid class: member well within limit
    (5, False),  # invalid class: member already at limit, 6th borrow rejected
])
def test_borrow_limit_classes(starting_count, should_succeed):
    lib = Library()
    lib.borrowed_counts["m1"] = starting_count
    if should_succeed:
        lib.borrow_book("m1", "9780134685991")
        assert lib.borrowed_counts["m1"] == starting_count + 1
    else:
        with pytest.raises(ValueError):
            lib.borrow_book("m1", "9780134685991")
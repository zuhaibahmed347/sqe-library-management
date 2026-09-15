import pytest
from gradebook import fine_tier  # adjust import path to your module

@pytest.mark.parametrize("days_overdue, expected", [
    (0, "None"),
    (1, "Low"),
    (7, "Low"),
    (8, "Medium"),
    (9, "Medium"),
    (14, "Medium"),
    (15, "High"),
    (16, "High"),
    (30, "High"),
    (31, "Severe"),
    (32, "Severe"),
])
def test_fine_tier_boundaries(days_overdue, expected):
    assert fine_tier(days_overdue) == expected

def test_fine_tier_negative_raises():
    with pytest.raises(ValueError):
        fine_tier(-1)

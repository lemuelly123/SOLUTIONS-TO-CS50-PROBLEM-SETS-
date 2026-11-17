import pytest
from seasons import get_days_diff, time_minutes_in_words


def test_get_days_diff_valid():
    assert get_days_diff("2025-11-17") == 525600
    assert get_days_diff("2024-11-17") == 1051200

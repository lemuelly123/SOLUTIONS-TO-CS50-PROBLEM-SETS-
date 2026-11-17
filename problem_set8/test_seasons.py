import pytest
from seasons import get_days_diff, time_minutes_in_words


def test_get_days_diff_valid():
    assert get_days_diff("2025-11-17") == 525600
    assert get_days_diff("2024-11-17") == 1051200

def test_get_days_diff_invalid():
    with pytest.raises(SystemExit) as exitinfo:
        get_days_diff("2024-12")
        get_days_diff ("12-12")
        get_days_diff("2021-01-")
        get_days_diff("")
        get_days_diff("hello")
    assert exitinfo.value.code == "Invalid format"

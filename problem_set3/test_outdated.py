import pytest
from outdated import (
    valid_day_month_year,
    get_date_from_user,
    MAX_MONTH,
    MAX_DAYS,
)

def test_valid_day_month_year():
    assert valid_day_month_year("1", "day") == 1
    assert valid_day_month_year("1", "month") == 1
    assert valid_day_month_year("2002", "year") == 2002

def test_invalid_day_month_year():
    with pytest.raises(ValueError):
        assert valid_day_month_year("32", "day")
        assert valid_day_month_year("13", "month")
        assert valid_day_month_year("", "year")


def test_get_date_from_user():
    assert get_date_from_user("12/4/1999") == "1999-04-12"
    assert get_date_from_user("1/1/2000") == "2000-01-01"
    assert get_date_from_user("March 15, 2012") == "2012-03-15"

def test_invalid_date_from_user():
    with pytest.raises(ValueError):
        assert get_date_from_user("12/0/1999")
        assert get_date_from_user("0/1/2000")
        assert get_date_from_user("-1/12/2000")
        assert get_date_from_user("")
        assert get_date_from_user(" /12/4444")
        assert get_date_from_user("9/ /2023")
        assert get_date_from_user("3/12/ ")
        assert get_date_from_user("32/12/2022")
        assert get_date_from_user("12/13/2022")
        
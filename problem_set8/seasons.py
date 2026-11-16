# the whole point of this problem is to create a program that calculates
# the entire minutes you have beeen alive assuming you start at midnight
# the day you were born
# user enter date formats as YYYY-MM-DD
import re, sys
from datetime import date


def convert_to_int(value, timestamp):
    if not isinstance(value, str):
        sys.exit(f"Invalid type for {timestamp}")
    value = value.strip()
    return int(value)


def get_minutes_diff(user_birthday):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    match = re.fullmatch(pattern, user_birthday)
    if not match:
        sys.exit()
    year, month, day = user_birthday.split("-")
    date_list = [
        convert_to_int(year, "year"),
        convert_to_int(month, "month"),
        convert_to_int(day, "day"),
    ]
    date1 = date.fromtimestamp(date_list[0]-date_list[1]-date_list[2])
    date2 = date.today()
    diff_in_minutes = (date2 - date1).min
    return 24 * 60 * diff_in_minutes



def main():
    user_birthday = input("Date of Birth: ").strip()
    tota_minutes = get_minutes_diff(user_birthday)


if __name__ == "__main__":
    main()

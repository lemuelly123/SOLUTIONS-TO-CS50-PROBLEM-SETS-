# the whole point of this problem is to create a program that calculates
# the entire minutes you have beeen alive assuming you start at midnight
# the day you were born
# user enter date formats as YYYY-MM-DD
import re, sys, inflect
from datetime import datetime


def get_days_diff(date):
    pattern = r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$"
    match = re.fullmatch(pattern, date)
    if not match:
        sys.exit("Invalid format")
    convert_to_int = lambda num:int(num)
    date_from_user = datetime(
        convert_to_int(match.group("year")), 
        convert_to_int(match.group("month")), 
        convert_to_int(match.group("day"))
        )
    date_today = datetime.today()
    diff_in_days = int((date_today - date_from_user).days)
    return 24 * 60 * diff_in_days


def time_minutes_in_words(minutes):
        num_words = inflect.engine()
        return f"{str(num_words.number_to_words(abs(minutes))).capitalize()} minutes"


def main():
    user_birthday = input("Date of Birth: ").strip()
    tota_minutes = get_days_diff(user_birthday)
    print(time_minutes_in_words(tota_minutes))


if __name__ == "__main__":
    main()

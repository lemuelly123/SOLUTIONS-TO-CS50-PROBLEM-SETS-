# the whole point of this problem is to create a program that calculates 
# the entire minutes you have beeen alive assuming you start at midnight 
# the day you were born
# user enter date formats as YYYY-MM-DD
import re, sys
from datetime import date


class BirthMinutes(date):
    def __init__(self, bday):
        self.bday = bday

    @property
    def bday(self):
        return self._bday
    @bday.setter
    def bday(self, date_of_birth):
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        match  = re.fullmatch(pattern, date_of_birth)
        if match:
            self._bday = date_of_birth
        else:
            sys.exit()
 
    def __str__(self):
        ...

    def get_bday_minutes(self):
        ...


def main():
    user_birthday = input("Date of Birth: ").strip()

    ...


if __name__ == "__main__":
    main()

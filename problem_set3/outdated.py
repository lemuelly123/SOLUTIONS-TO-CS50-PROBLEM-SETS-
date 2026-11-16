months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
MAX_DAYS = 31
MAX_MONTH = 12


def valid_day_month_year(value, timestamp):
    time = {"day": MAX_DAYS, "month": MAX_MONTH}
    value = value.strip()
    if not value.isdigit():
        raise ValueError(f"Expected number for {timestamp} but got {value!r} instead")
    value = int(value)
    if timestamp in ["day", "month"]:
        if value > time[timestamp]:
            raise ValueError(f"{timestamp} cannot exceed {time[timestamp]}")
        elif value == 0:
           raise ValueError(f"{timestamp} cannot be {value!r}") 
    elif timestamp == "year":
        return value
    return value


def get_date_from_user(date):
    if "/" in date:
        day, month, year = date.split("/")
        d = valid_day_month_year(day, "day")
        m = valid_day_month_year(month, "month")
        y = valid_day_month_year(year, "year")
        return f"{y}-{m:02}-{d:02}"
    elif "," in date:
        month_index = 0
        month_day, year = date.split(",")
        month, day = month_day.split(" ")
        month = month.strip().title()
        if month not in months:
            raise ValueError("Invalid month")
        d = valid_day_month_year(day, "day")
        y = valid_day_month_year(year, "year")
        for i in range(len(months)):
            if months[i] == month:
                month_index = i + 1
        return f"{y}-{month_index:02}-{d:02}"
    else:
        raise ValueError(
            f"Invalid date format expected [m d, y] or [dd/mm/yyyy] but got {date!r} instead"
        )


# user format in either Month day, year or
# DD/MM/YYYY
# ouput in YYYY-MM-DD
def main():
    user_date = input("Date: ").strip()

    try:
        date = get_date_from_user(user_date)
        print(date)
    except ValueError as v:
        print(v)


if __name__ == "__main__":
    main()

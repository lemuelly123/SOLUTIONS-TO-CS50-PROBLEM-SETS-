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

def valid_parameter(value, timestamp):
    value = value.strip()
    if not value.isdigit():
            raise ValueError(f"Expected number for {timestamp} but got {value!r} instead")
    return int(value)

def valid_month(month):
    month = month.strip().title()
    if month not in months:
        raise ValueError("Invalid month")
    return month

def get_date_from_user(date):
    if "/" in date:
            day, month, year = date.split("/")
            d = valid_parameter(day, "day")
            m = valid_parameter(month, "month")
            y = valid_parameter(year, "year")
            return f"{y}-{m}-{d}"
    elif "," in date:
        month_index = 0
        month_day, year = date.split(",")
        month, day = month_day.split(" ")
        m = valid_month(month)
        d = valid_parameter(day, "day")
        y = valid_parameter(year, "month")
        for i in range(len(months)):
              if months[i] == m:
                month_index = i + 1
        return f"{y}-{month_index}-{d}"
    else:
         raise ValueError(f"Invalid date format expected [m d, y] or [dd/mm/yyyy] but got {date!r} instead")
                    

def main():
    user_date = input("Date: ").strip()
    # user format in either Month day, year or 
    # DD/MM/YYYY
    # ouput in YYYY-MM-DD
    try:
        date = get_date_from_user(user_date)
        print(date)
    except ValueError as v:
         print(v)
if __name__ == "__main__":
    main()
HOUR_LIMIT = 24
MINUTE_LIMIT = 60


def main():
    time = input("What time is it? ").strip()
    try:
        converted_time = convert(time)
        if 7 <= converted_time <= 8:
            print("Breakfast time")
        elif 12 <= converted_time <= 13:
            print("Lunch time")
        elif 18 <= converted_time <= 19:
            print("Dinner")
        else:
            print("Chill")
    except ValueError as v:
        print(v)


def convert(time):
    # hour = hour + min/60
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    if hour > HOUR_LIMIT:
        raise ValueError(f"Hour cannot exceed {HOUR_LIMIT}")
    if hour < 0:
        raise ValueError(f"Hour cannot be negative")
    if minute > MINUTE_LIMIT:
        raise ValueError(f"Minute cannot exceed {MINUTE_LIMIT}")
    if minute < 0:
        raise ValueError(f"Minute cannot be negative")
    full_time = hour + (minute / MINUTE_LIMIT)
    return full_time


if __name__ == "__main__":
    main()

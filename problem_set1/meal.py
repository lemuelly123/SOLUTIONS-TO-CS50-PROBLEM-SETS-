def main():
    time = input("What time is it? ").strip()
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("Breakfast time")
    elif 12 <= converted_time <= 13:
        print("Lunch time")
    elif 18 <= converted_time <= 19:
        print("Dinner")
    else:
        print("Chill")


def convert(time):
    # hour = hour + min/60
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    if not 0 <= hour <= 24:
        ...
    if not 0 <= minute <= 60:
        ...
    full_time = hour + (minute / 60)
    return full_time



if __name__ == "__main__":
    main()

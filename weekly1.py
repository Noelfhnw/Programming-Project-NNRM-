"""Weekly Sleep Tracker (US-06, US-07, US-08, US-09).

This file reads the same sleep_data.json used by add_Sleep_data.py.
It also adds an OPTIONAL weekly sleep score for the project.
"""

import json
from datetime import date


# This is the order used by your team's sleep_data.json file.
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# The group decided that the Weekly view needs at least four complete nights.
MIN_NIGHTS = 4


def load_sleep_data():
    # Open the JSON file and convert its contents into a Python dictionary.
    # We read the file directly because importing add_Sleep_data.py currently
    # starts its input menu automatically (see the bottom of that file).
    try:
        with open("sleep_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, dict):
            print("Sleep data has the wrong format.")
            return {}
        return data
    except FileNotFoundError:
        print("No sleep_data.json file found. Enter sleep data first.")
        return {}
    except (json.JSONDecodeError, OSError):
        print("Could not read sleep_data.json. Please check the file.")
        return {}


def time_to_minutes(time_text):
    # Convert a clock time such as "23:30" into minutes since midnight.
    # 23 * 60 + 30 = 1410 minutes. Invalid times raise ValueError.
    if not isinstance(time_text, str) or len(time_text) != 5:
        raise ValueError("Time must use HH:MM")
    if time_text[2] != ":":
        raise ValueError("Time must use HH:MM")

    hours_text, minutes_text = time_text.split(":")
    if not hours_text.isdigit() or not minutes_text.isdigit():
        raise ValueError("Time must contain numbers")

    hours = int(hours_text)
    minutes = int(minutes_text)
    if hours > 23 or minutes > 59:
        raise ValueError("Time is outside the allowed range")

    return hours * 60 + minutes


def fall_asleep_to_minutes(value):
    # Your CURRENT input file saves fall-asleep time as HH:MM (e.g. "00:20").
    # The project plan mentions whole minutes, so we support "20" as well.
    if isinstance(value, int) and not isinstance(value, bool):
        minutes = value
    elif isinstance(value, str) and value.strip().isdigit():
        minutes = int(value.strip())
    else:
        minutes = time_to_minutes(value)

    if minutes < 0 or minutes >= 1440:
        raise ValueError("Invalid fall-asleep duration")
    return minutes


def calculate_sleep_minutes(record):
    # Work out how long someone actually slept, including across midnight.
    # Example: 23:30 to 07:00 is 450 minutes in bed.
    # If falling asleep took 20 minutes, actual sleep is 430 minutes.
    try:
        bed = time_to_minutes(record.get("Bedtime"))
        wake = time_to_minutes(record.get("Wake-up time"))
        falling_asleep = fall_asleep_to_minutes(record.get("Time to fall asleep"))
    except (ValueError, TypeError, AttributeError):
        return None  # Missing or incorrect input: do not use this night.

    time_in_bed = (wake - bed) % 1440  # % handles a midnight crossing.
    sleep_minutes = time_in_bed - falling_asleep

    if sleep_minutes <= 0:
        return None  # A sleep duration of zero or less is not usable.
    return sleep_minutes


def format_duration(minutes):
    # Turn 430 minutes into text such as "7h 10min".
    minutes = round(minutes)
    return f"{minutes // 60}h {minutes % 60:02d}min"


def format_clock(minutes):
    # Turn minutes into a clock time such as "23:30".
    # Modulo (%) also keeps values within a 24-hour day.
    minutes = round(minutes) % 1440
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def clock_difference(time_minutes, reference_minutes):
    # Find the shortest SIGNED difference between two times on a clock.
    # Example: 23:30 compared with 00:00 is -30 minutes, not +1410.
    # A negative result means earlier; a positive result means later.
    return (time_minutes - reference_minutes + 720) % 1440 - 720


def average_clock(times):
    # Average clock times correctly when they cross midnight.
    # Normal averaging fails for 23:30 and 00:30 (it gives 12:00).
    # We first compare every time with the first value, then average.
    first_time = times[0]
    total_difference = 0
    for one_time in times:
        total_difference += clock_difference(one_time, first_time)
    return round(first_time + total_difference / len(times)) % 1440


def prepare_weekly_entries(data):
    # Build a list containing only nights with valid bedtime, wake-up time,
    # and time-to-fall-asleep values. An incomplete day is skipped safely.
    entries = []
    for day in DAYS:
        record = data.get(day)
        if not isinstance(record, dict):
            continue

        sleep_minutes = calculate_sleep_minutes(record)
        if sleep_minutes is None:
            continue

        bedtime = time_to_minutes(record["Bedtime"])
        wake_time = time_to_minutes(record["Wake-up time"])

        # Morning ratings are stored as text in the current input program.
        # They can be missing; we only use ratings between 1 and 5.
        rating = record.get("Morning rating")
        if str(rating) in ["1", "2", "3", "4", "5"]:
            rating = int(rating)
        else:
            rating = None

        entries.append({
            "day": day,
            "bedtime": bedtime,
            "wake_time": wake_time,
            "sleep_minutes": sleep_minutes,
            "rating": rating,
        })

    return entries


def average_sleep_minutes(entries):
    # Add all durations and divide by the number of recorded nights.
    total = 0
    for entry in entries:
        total += entry["sleep_minutes"]
    return round(total / len(entries))


def show_weekly_average(entries):
    # US-06: Display average sleep duration for the recorded week.
    average = average_sleep_minutes(entries)
    count = len(entries)
    print(f"Weekly average: {format_duration(average)} ({count} nights)")
    return average


def show_longest_shortest(entries):
    # US-07: Find the nights with the highest and lowest sleep durations.
    # Starting with the first entry avoids needing a special number like 0.
    longest = entries[0]
    shortest = entries[0]
    for entry in entries:
        if entry["sleep_minutes"] > longest["sleep_minutes"]:
            longest = entry
        if entry["sleep_minutes"] < shortest["sleep_minutes"]:
            shortest = entry

    print(f"Longest night:  {longest['day']} ({format_duration(longest['sleep_minutes'])})")
    print(f"Shortest night: {shortest['day']} ({format_duration(shortest['sleep_minutes'])})")


def get_average_times(entries):
    # US-08 helper: Put bedtimes and wake-up times into separate lists.
    # The average_clock function handles times near midnight.
    bedtimes = []
    wake_times = []
    for entry in entries:
        bedtimes.append(entry["bedtime"])
        wake_times.append(entry["wake_time"])
    return average_clock(bedtimes), average_clock(wake_times)


def describe_difference(minutes):
    # Turn a signed difference into readable text for the user.
    if minutes < 0:
        return f"{abs(minutes)}min earlier"
    elif minutes > 0:
        return f"{minutes}min later"
    else:
        return "0min difference"


def show_rhythm(entries):
    # US-08: Show the average bedtime and wake-up time for the week.
    avg_bed, avg_wake = get_average_times(entries)
    print(f"Average bedtime: {format_clock(avg_bed)}")
    print(f"Average wake-up: {format_clock(avg_wake)}")

    # Compare yesterday's weekday entry with the averages, if it exists.
    # Note: JSON has only weekday names, not dates; this assumes entries
    # belong to the current week (the file cannot verify their age).
    yesterday = DAYS[(date.today().weekday() - 1) % 7]
    for entry in entries:
        if entry["day"] == yesterday:
            bed_diff = clock_difference(entry["bedtime"], avg_bed)
            wake_diff = clock_difference(entry["wake_time"], avg_wake)
            print(f"{yesterday} bedtime: {describe_difference(bed_diff)} than average" if bed_diff != 0
                  else f"{yesterday} bedtime: 0min difference from average")
            print(f"{yesterday} wake-up: {describe_difference(wake_diff)} than average" if wake_diff != 0
                  else f"{yesterday} wake-up: 0min difference from average")
            return
    print("Yesterday's weekday has no complete entry for comparison.")


def show_recommendation(entries):
    # US-09: Recommend a bedtime based on the week's average wake-up time.
    # The project plan uses: ideal bedtime = average wake-up time - 8 hours.
    avg_bed, avg_wake = get_average_times(entries)
    ideal_bed = (avg_wake - 8 * 60) % 1440
    print("Sleep target: 8h 00min")
    print(f"Ideal bedtime: {format_clock(ideal_bed)}")
    print("Tip: Keep your bedtime and wake-up time reasonably consistent.")


def show_weekly_score(entries):
    # BONUS (not an official user story): estimate a weekly score from 0-100.
    # We use the familiar 50/30/20 weighting from the daily readiness score.
    # 50 points = average sleep duration, capped at 8 hours.
    # 30 points = average morning rating (1-5).
    # 20 points = fraction of nights within 30min of average bedtime.
    # This is only a simple project estimate, not a medical assessment.
    ratings = []
    for entry in entries:
        if entry["rating"] is not None:
            ratings.append(entry["rating"])

    # Do not present a complete weekly score if some ratings are missing.
    if len(ratings) != len(entries):
        print("Weekly score unavailable: add a morning rating for every recorded night.")
        return

    average_minutes = average_sleep_minutes(entries)
    duration_points = min(average_minutes / 480, 1) * 50
    quality_points = (sum(ratings) / len(ratings)) / 5 * 30

    average_bed, average_wake = get_average_times(entries)
    consistent_nights = 0
    for entry in entries:
        difference = abs(clock_difference(entry["bedtime"], average_bed))
        if difference <= 30:
            consistent_nights += 1

    consistency_points = consistent_nights / len(entries) * 20
    score = round(duration_points + quality_points + consistency_points)

    print(f"Weekly sleep score: {score}/100 (simple estimate)")
    print(f"  Duration:    {duration_points:.1f}/50 points")
    print(f"  Quality:     {quality_points:.1f}/30 points")
    print(f"  Consistency: {consistency_points:.1f}/20 points")
    print(f"Consistent bedtimes: {consistent_nights} of {len(entries)} nights (within 30min)")


def weekly(data=None):
    # Main function: called when the user chooses option 3 in main.py.
    # By default, it loads saved JSON. Passing data is useful for tests.
    if data is None:
        data = load_sleep_data()

    print("\n========== WEEKLY SLEEP REVIEW ==========")
    entries = prepare_weekly_entries(data)
    print(f"Complete nights: {len(entries)} of 7")

    # The team requires four complete nights for the Weekly view.
    if len(entries) < MIN_NIGHTS:
        print(f"At least {MIN_NIGHTS} complete nights are needed for a weekly review.")
        print("Add bedtime, wake-up time, and fall-asleep time for more days.")
        return

    print("\n--- Sleep duration (US-06) ---")
    # Show the duration of each recorded night before the weekly average.
    for entry in entries:
        print(f"{entry['day']}: {format_duration(entry['sleep_minutes'])}")
    show_weekly_average(entries)
    print("\n--- Longest and shortest night (US-07) ---")
    show_longest_shortest(entries)
    print("\n--- Sleep rhythm (US-08) ---")
    show_rhythm(entries)
    print("\n--- Sleep recommendation (US-09) ---")
    show_recommendation(entries)
    print("\n--- Bonus weekly score ---")
    show_weekly_score(entries)
    print("=========================================\n")


# Run the review directly with: python weekly.py
# When main.py imports this file, this block does NOT run automatically.
if __name__ == "__main__":
    weekly()

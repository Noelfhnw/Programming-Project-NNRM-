import add_Sleep_data
from datetime import date
import os

# ==========================================
# Time conversion and sleep calculations
# ==========================================

MIN_NIGHTS = 4

# Convert time from HH:MM to minutes
def time_to_minutes(time):
    # Check if the time is valid
    if not isinstance(time, str) or not add_Sleep_data.time_input_valid_bedtime_data(time):
        return None

    hours = int(time[0:2])
    minutes = int(time[3:5])

    #print("Hours:", hours)
    #print("Minutes:", minutes)

    return hours * 60 + minutes


# Get sleep times for a selected day and convert them to minutes
def get_sleep_times(data, day):
    bedtime = time_to_minutes(data[day]["Bedtime"])
    wake_up = time_to_minutes(data[day]["Wake-up time"])
    # Fall asleep duration is already stored in minutes
    fall_asleep = data[day]["Minutes to fall asleep"]

    return bedtime, wake_up, fall_asleep

# # Test
# data = add_Sleep_data.load_data()

# print(get_sleep_times(data, "Monday"))

# Calculate sleep duration in minutes for a selected day
def calculate_sleep_duration(data, day):
    bedtime, wake_up, fall_asleep = get_sleep_times(data, day)

    if bedtime is None or wake_up is None or fall_asleep is None:
        return None

    # Handle sleep across midnight
    if wake_up < bedtime:
        wake_up += 24 * 60

    duration = wake_up - bedtime - fall_asleep

    if duration <= 0:
        return None

    return duration

# Test
# data = add_Sleep_data.load_data()

# print("Original data:", data["Monday"])
# print("Converted times:", get_sleep_times(data, "Monday"))
# print("Sleep duration:", calculate_sleep_duration(data, "Monday"))
# Calculate total time in bed for a selected day

def calculate_time_in_bed(data, day):

    # Get sleep times in minutes
    bedtime, wake_up, _ = get_sleep_times(data, day)

    # Check if data is available
    if bedtime is None or wake_up is None:
        return None

    # Handle sleep across midnight
    if wake_up < bedtime:
        wake_up += 24 * 60

    # Calculate total time in bed
    return wake_up - bedtime


# Test
# data = add_Sleep_data.load_data()

# print("Time in bed:", calculate_time_in_bed(data, "Monday"))
# print("Sleep duration:", calculate_sleep_duration(data, "Monday"))


def format_sleep_duration(duration):

    # Check if duration is available
    if duration is None:
        return "Not available"

    # Convert minutes to hours and minutes
    hours = duration // 60
    minutes = duration % 60

    # Return formatted sleep duration
    return f"{hours}h {minutes:02d}min"

# Test
# print(format_sleep_duration(360))
# print(format_sleep_duration(465))
# print(format_sleep_duration(90))
# print(format_sleep_duration(0))
# print(format_sleep_duration(None))

# Calculate sleep efficiency for a selected day
def calculate_sleep_efficiency(data, day):

    # Get calculated sleep duration and time in bed
    duration = calculate_sleep_duration(data, day)
    time_in_bed = calculate_time_in_bed(data, day)

    # Check if data is available
    if duration is None or time_in_bed is None:
        return None

    # Prevent division by zero
    if time_in_bed == 0:
        return None

    # Calculate sleep efficiency
    efficiency = duration / time_in_bed * 100

    return round(efficiency, 2)
# Test
# data = add_Sleep_data.load_data()

# for day in add_Sleep_data.days:
#     print(day, calculate_sleep_efficiency(data, day))

# Generate a unique filename for the weekly report
def next_file():
    number = 1

    while os.path.exists(f"exports/weekly_{number:03d}.txt"):
        number += 1

    return f"exports/weekly_{number:03d}.txt"

# Generate and save the weekly sleep report
def weekly_overview():

    # Load saved sleep data from the JSON file
    data_w = add_Sleep_data.load_data()

    # Create the export folder if it does not exist
    os.makedirs("exports", exist_ok=True)

    # Generate a new filename
    filename = next_file()

    # Open the TXT file in write mode
    with open(filename, "w", encoding="utf-8") as file:

        # Write the report title
        file.write("=== Weekly Sleep Report ===\n\n")

        # Write sleep data for each day
        for day in add_Sleep_data.days:
            file.write(f"{day}\n")
            file.write("--- Calculated results ---\n")

            # Calculate and format sleep duration
            duration = calculate_sleep_duration(data_w, day)
            formatted_duration = format_sleep_duration(duration)

            file.write(f"Sleep duration: {formatted_duration}\n")

            # Calculate and format total time in bed
            time_in_bed = calculate_time_in_bed(data_w, day)
            formatted_time_in_bed = format_sleep_duration(time_in_bed)

            file.write(f"Time in bed: {formatted_time_in_bed}\n")

            # Calculate sleep efficiency
            efficiency = calculate_sleep_efficiency(data_w, day)

            # Format sleep efficiency
            if efficiency is None:
                formatted_efficiency = "Not available"
            else:
                formatted_efficiency = f"{efficiency}%"

            file.write(f"Sleep efficiency: {formatted_efficiency}\n")

            # Separate the days
            file.write("\n-----------------------------------\n\n")

        # Prepare weekly entries
        entries = prepare_weekly_entries(data_w)

        # Generate weekly summary
        summary = weekly_summary(entries)

        # Write weekly summary at the end of the report
        file.write(summary)
        file.write("\n")

    print("\n----------------------------------------------\n")
    print("Weekly report successfully exported!")
    print("")
    print(f"File saved to: {filename}")
    print("\n----------------------------------------------\n")

#     # Test
# weekly_overview()

# ==========================================
# Prepare weekly data
# ==========================================

# Collect all nights with complete sleep data
def prepare_weekly_entries(data):

    entries = []

    for day in add_Sleep_data.days:

        # Calculate sleep duration
        duration = calculate_sleep_duration(data, day)

        # Skip incomplete nights
        if duration is None:
            continue

        # Get sleep times in minutes
        bedtime, wake_up, fall_asleep = get_sleep_times(data, day)

        # Calculate time in bed and sleep efficiency
        time_in_bed = calculate_time_in_bed(data, day)
        efficiency = calculate_sleep_efficiency(data, day)

        # Get and validate morning rating
        rating = data[day]["Morning rating"]

        if str(rating) in ["1", "2", "3", "4", "5"]:
            rating = int(rating)
        else:
            rating = None

        # Add the calculated results to the list
        entries.append({
            "day": day,
            "bedtime": bedtime,
            "wake_time": wake_up,
            "fall_asleep": fall_asleep,
            "sleep_minutes": duration,
            "time_in_bed": time_in_bed,
            "efficiency": efficiency,
            "rating": rating
        })

    return entries

# Test
# data = add_Sleep_data.load_data()

# entries = prepare_weekly_entries(data)

# for entry in entries:
#     print(entry)

# print("Complete nights:", len(entries))

# Calculate the average value for a selected field
def calculate_average(entries, field):

    values = []

    # Collect available values
    for entry in entries:
        if entry[field] is not None:
            values.append(entry[field])

    # Check if values are available
    if len(values) == 0:
        return None

    # Calculate the average
    return sum(values) / len(values)

# Test
# data = add_Sleep_data.load_data()
# entries = prepare_weekly_entries(data)

# print("Average sleep duration:", format_sleep_duration(round(calculate_average(entries, "sleep_minutes"))))
# print("Average time in bed:", format_sleep_duration(round(calculate_average(entries, "time_in_bed"))))
# print("Average sleep efficiency:", round(calculate_average(entries, "efficiency"), 2))
# print("Average morning rating:", calculate_average(entries, "rating"))
# print("Average time to fall asleep:", format_sleep_duration(round(calculate_average(entries, "fall_asleep"))))

# Calculate total sleep duration for all recorded nights
def calculate_total_sleep_duration(entries):

    # Check if entries are available
    if len(entries) == 0:
        return None

    total = 0

    # Add sleep duration for each recorded night
    for entry in entries:
        total += entry["sleep_minutes"]

    return total

# Test
# data = add_Sleep_data.load_data()
# entries = prepare_weekly_entries(data)

# total = calculate_total_sleep_duration(entries)

# print("Total sleep duration in minutes:", total)
# print("Total sleep duration:", format_sleep_duration(total))

# Find the longest and shortest sleep duration
def get_longest_shortest(entries):

    # Check if entries are available
    if len(entries) == 0:
        return None, None

    # Start with the first recorded night
    longest = entries[0]
    shortest = entries[0]

    # Compare sleep duration for each night
    for entry in entries:

        if entry["sleep_minutes"] > longest["sleep_minutes"]:
            longest = entry

        if entry["sleep_minutes"] < shortest["sleep_minutes"]:
            shortest = entry

    return longest, shortest

# Test
# data = add_Sleep_data.load_data()
# entries = prepare_weekly_entries(data)

# longest, shortest = get_longest_shortest(entries)

# if longest is not None:
#     print("Longest night:", longest["day"])
#     print("Sleep duration:", format_sleep_duration(longest["sleep_minutes"]))

#     print("Shortest night:", shortest["day"])
#     print("Sleep duration:", format_sleep_duration(shortest["sleep_minutes"]))
# else:
#     print("Not available")

# Convert minutes to HH:MM clock format
def format_clock(minutes):

    # Check if data is available
    if minutes is None:
        return "Not available"

    # Keep time within a 24-hour day
    minutes = round(minutes) % 1440

    hours = minutes // 60
    minutes = minutes % 60

    return f"{hours:02d}:{minutes:02d}"

# Test
# print(format_clock(1410))
# print(format_clock(425))
# print(format_clock(1440))
# print(format_clock(1470))
# print(format_clock(None))

# Calculate the shortest time difference across midnight
def clock_difference(time_minutes, reference_minutes):

    return (time_minutes - reference_minutes + 720) % 1440 - 720

# Test
# print(clock_difference(time_to_minutes("00:30"), time_to_minutes("23:30")))

# print(clock_difference(time_to_minutes("23:30"), time_to_minutes("00:30")))

# print(clock_difference(time_to_minutes("22:00"), time_to_minutes("21:30")))

# print(clock_difference(time_to_minutes("07:00"), time_to_minutes("07:00")))

# Calculate average clock time across midnight
def average_clock(times):

    # Check if times are available
    if len(times) == 0:
        return None

    # Use the first time as a reference
    reference_time = times[0]

    total_difference = 0

    # Calculate the difference for each time
    for time in times:
        total_difference += clock_difference(time, reference_time)

    # Calculate the average difference
    average_difference = total_difference / len(times)

    # Calculate the average clock time
    return round(reference_time + average_difference) % 1440

# Test
# times = [
#     time_to_minutes("23:30"),
#     time_to_minutes("00:30")
# ]

# average = average_clock(times)

# print("Average in minutes:", average)
# print("Average clock time:", format_clock(average))
# print(format_clock(average_clock([1380, 60])))
# print(format_clock(average_clock([360, 480])))
# print(format_clock(average_clock([420])))
# print(format_clock(average_clock([])))

# Calculate average bedtime and wake-up time
def get_average_times(entries):

    bedtimes = []
    wake_times = []

    # Collect bedtime and wake-up time for each night
    for entry in entries:
        bedtimes.append(entry["bedtime"])
        wake_times.append(entry["wake_time"])

    # Calculate average clock times
    average_bedtime = average_clock(bedtimes)
    average_wake_up = average_clock(wake_times)

    return average_bedtime, average_wake_up

# Test
# data = add_Sleep_data.load_data()
# entries = prepare_weekly_entries(data)

# average_bedtime, average_wake_up = get_average_times(entries)

# print("Average bedtime in minutes:", average_bedtime)
# print("Average wake-up time in minutes:", average_wake_up)

# print("Average bedtime:", format_clock(average_bedtime))
# print("Average wake-up time:", format_clock(average_wake_up))

# Describe the difference from the average clock time
def describe_difference(minutes):

    if minutes is None:
        return "Not available"

    if minutes < 0:
        return f"{abs(minutes)}min earlier than average"

    elif minutes > 0:
        return f"{minutes}min later than average"

    else:
        return "Same as average"

# # Test
# print(describe_difference(-30))
# print(describe_difference(45))
# print(describe_difference(0))
# print(describe_difference(None))
# # Test
# bedtime = time_to_minutes("00:30")
# average_bedtime = time_to_minutes("23:30")

# difference = clock_difference(bedtime, average_bedtime)

# print(describe_difference(difference))

# Calculate recommended bedtime for 8 hours of sleep
def calculate_ideal_bedtime(average_wake_up):

    # Check if data is available
    if average_wake_up is None:
        return None

    # Recommended sleep duration in minutes
    target_sleep = 8 * 60

    # Calculate bedtime across midnight
    return (average_wake_up - target_sleep) % 1440

# # Test
# data = add_Sleep_data.load_data()
# entries = prepare_weekly_entries(data)

# average_bedtime, average_wake_up = get_average_times(entries)

# ideal_bedtime = calculate_ideal_bedtime(average_wake_up)

# print("Average wake-up time:", format_clock(average_wake_up))
# print("Recommended bedtime:", format_clock(ideal_bedtime))
# print(format_clock(calculate_ideal_bedtime(time_to_minutes("07:00"))))
# print(format_clock(calculate_ideal_bedtime(time_to_minutes("09:30"))))
# print(format_clock(calculate_ideal_bedtime(None)))

# Calculate the weekly sleep score
def calculate_weekly_score(entries):

    # Check if entries are available
    if len(entries) == 0:
        return None

    # Check if all morning ratings are available
    for entry in entries:
        if entry["rating"] is None:
            return None

    # Calculate sleep duration points (max 50)
    average_duration = calculate_average(entries, "sleep_minutes")
    duration_points = min(average_duration / 480, 1) * 50

    # Calculate morning rating points (max 30)
    average_rating = calculate_average(entries, "rating")
    quality_points = average_rating / 5 * 30

    # Calculate sleep consistency points (max 20)
    average_bedtime, _ = get_average_times(entries)

    consistent_nights = 0

    for entry in entries:
        difference = abs(clock_difference(
            entry["bedtime"], average_bedtime
        ))

        if difference <= 30:
            consistent_nights += 1

    consistency_points = consistent_nights / len(entries) * 20

    # Calculate total weekly score
    score = round(duration_points + quality_points + consistency_points)

    return score, duration_points, quality_points, consistency_points, consistent_nights

# # Test
# data = add_Sleep_data.load_data()
# entries = prepare_weekly_entries(data)

# score = calculate_weekly_score(entries)

# print("Weekly sleep score:", score)


# Generate weekly summary
def weekly_summary(entries):

    lines = []

    lines.append("\n========== WEEKLY SLEEP REVIEW ==========\n")
    lines.append(f"Complete nights: {len(entries)} of 7")

    # Check the minimum number of recorded nights
    if len(entries) < MIN_NIGHTS:
        lines.append(f"At least {MIN_NIGHTS} complete nights are required.")
        lines.append(f"Add bedtime, wake-up time, and fall-asleep time for more days.")
        return "\n".join(lines)

    # Calculate weekly statistics
    total = calculate_total_sleep_duration(entries)
    average_duration = calculate_average(entries, "sleep_minutes")
    average_time_in_bed = calculate_average(entries, "time_in_bed")
    average_efficiency = calculate_average(entries, "efficiency")

    lines.append(f"Total sleep duration: {format_sleep_duration(total)}")
    lines.append(f"Average sleep duration: {format_sleep_duration(round(average_duration))}")
    lines.append(f"Average time in bed: {format_sleep_duration(round(average_time_in_bed))}")
    lines.append(f"Average sleep efficiency: {average_efficiency:.2f}%")

    # Longest and shortest nights
    longest, shortest = get_longest_shortest(entries)

    lines.append("\n--- Longest and Shortest Nights ---")
    lines.append(f"Longest night: {longest['day']}")
    lines.append(f"Sleep duration: {format_sleep_duration(longest['sleep_minutes'])}")
    lines.append(f"Shortest night: {shortest['day']}")
    lines.append(f"Sleep duration: {format_sleep_duration(shortest['sleep_minutes'])}")

    # Average bedtime and wake-up time
    average_bedtime, average_wake_up = get_average_times(entries)

    lines.append("\n--- Sleep Rhythm ---")
    lines.append(f"Average bedtime: {format_clock(average_bedtime)}")
    lines.append(f"Average wake-up time: {format_clock(average_wake_up)}")

    # Compare yesterday's sleep rhythm with average times
    yesterday = add_Sleep_data.days[(date.today().weekday() - 1) % 7]

    for entry in entries:
        if entry["day"] == yesterday:

            bedtime_difference = clock_difference(
                entry["bedtime"], average_bedtime
            )

            wake_up_difference = clock_difference(
                entry["wake_time"], average_wake_up
            )

            lines.append(f"Yesterday: {yesterday}")
            lines.append(f"Bedtime: {describe_difference(bedtime_difference)}")
            lines.append(f"Wake-up time: {describe_difference(wake_up_difference)}")
            break
    else:
        lines.append("Yesterday's sleep data: Not available")

    # Sleep recommendation
    ideal_bedtime = calculate_ideal_bedtime(average_wake_up)

    lines.append("\n--- Sleep Recommendation ---")
    lines.append("Target sleep duration: 8 hours")
    lines.append(f"Recommended bedtime: {format_clock(ideal_bedtime)}")
    lines.append("Try to maintain a consistent sleep schedule.")

    # Weekly sleep score
    # BONUS (not an official user story): estimate a weekly score from 0-100.
    # We use the familiar 50/30/20 weighting from the daily readiness score.
    # 50 points = average sleep duration, capped at 8 hours.
    # 30 points = average morning rating (1-5).
    # 20 points = fraction of nights within 30min of average bedtime.
    # This is only a simple project estimate, not a medical assessment.
    score_result = calculate_weekly_score(entries)

    lines.append("\n--- Weekly Sleep Score ---")

    if score_result is None:
        lines.append("Weekly score unavailable: add a morning rating for every recorded night")
    else:
        score, duration_points, quality_points, consistency_points, consistent_nights = score_result

        lines.append(f"Weekly sleep score: {score}/100 (simple estimate)")
        lines.append(f"Duration:    {duration_points:.1f}/50 points")
        lines.append(f"Quality:     {quality_points:.1f}/30 points")
        lines.append(f"Consistency: {consistency_points:.1f}/20 points")
        lines.append(f"Consistent bedtimes: {consistent_nights} of {len(entries)} nights (within 30min)")

    return "\n".join(lines)

# Test
# data = add_Sleep_data.load_data()
# entries = prepare_weekly_entries(data)

# print(weekly_summary(entries))

# Display weekly analysis and export options
def weekly():

    # Load saved sleep data
    data = add_Sleep_data.load_data()

    # Prepare weekly entries
    entries = prepare_weekly_entries(data)

    # Display weekly summary
    print("\n----------------------------------------------\n")
    print(weekly_summary(entries))

    # Display available options
    while True:

        print("""
----------------------------------------------

What would you like to do?

1. Export to text file
2. Exit to main menu
        """)

        choice = input("Choose an option: ")

        if choice == "1":
            weekly_overview()

        elif choice == "2":
            break

        else:
            print("Invalid input! Choose 1 or 2.")


# Test
if __name__ == "__main__":
    weekly()
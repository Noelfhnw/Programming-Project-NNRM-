import add_Sleep_data

# Convert time from HH:MM to minutes
def time_to_minutes(time):
    hours = int(time[0:2])
    minutes = int(time[3:5])

    return hours * 60 + minutes


# Get sleep times for a selected day and convert them to minutes
def get_sleep_times(data, day):
    bedtime = data[day]["Bedtime"]
    wake_up = data[day]["Wake-up time"]
    fall_asleep = data[day]["Time to fall asleep"]

    if bedtime is not None:
        bedtime = time_to_minutes(bedtime)

    if wake_up is not None:
        wake_up = time_to_minutes(wake_up) + 24 * 60

    if fall_asleep is not None:
        fall_asleep = time_to_minutes(fall_asleep)

    return bedtime, wake_up, fall_asleep


# Calculate sleep duration in minutes for a selected day
def calculate_sleep_duration(data, day):
    bedtime, wake_up, fall_asleep = get_sleep_times(data, day)

    if bedtime is None or wake_up is None or fall_asleep is None:
        return None

    duration = wake_up - bedtime - fall_asleep
    # print("Actual sleep duration:", duration)

    if duration < 0:
        return None

    return duration


# Convert sleep duration from minutes to hours and minutes
def format_sleep_duration(duration):

    # Check if duration is available
    if duration is None:
        return "Not available"

    # Convert minutes to hours and minutes
    hours = duration // 60
    minutes = duration % 60

    # Return formatted sleep duration
    return f"{hours}h {minutes}min"


# Generate and save the weekly sleep report
def weekly_overview():

    # Load saved sleep data from the JSON file
    data_w = add_Sleep_data.load_data()

    # Open the TXT file in write mode
    with open("weekly_data.txt", "w", newline="") as file:

        # Write the report title
        file.write("=== Weekly Sleep Report ===\n\n")

        # Write sleep data for each day
        for day in add_Sleep_data.days:
            file.write(f"{day}\n")

            for field, value in data_w[day].items():
                file.write(f"{field}: {value}\n")

            file.write("\n--- Calculated results ---\n")

            # Calculate and format sleep duration
            duration = calculate_sleep_duration(data_w, day)
            formatted_duration = format_sleep_duration(duration)

            print(f"Sleep duration: {formatted_duration}")
            # Write sleep duration to the report
            file.write(f"Sleep duration: {formatted_duration}\n")

            # Calculate and format total time in bed
            time_in_bed = calculate_time_in_bed(data_w, day)
            formatted_time_in_bed = format_sleep_duration(time_in_bed)

            print(f"Time in bed: {formatted_time_in_bed}")
            # Write time in bed to the report
            file.write(f"Time in bed: {formatted_time_in_bed}\n")

            # Calculate sleep efficiency
            efficiency = calculate_sleep_efficiency(data_w, day)

            # Format sleep efficiency
            if efficiency is None:
                formatted_efficiency = "Not available"
            else:
                formatted_efficiency = f"{efficiency}%"

            print(f"Sleep efficiency: {formatted_efficiency}")

            # Write sleep efficiency to the report
            file.write(f"Sleep efficiency: {formatted_efficiency}\n")

            file.write("\n")

    print("Weekly report saved successfully!")

# Calculate total time in bed for a selected day
def calculate_time_in_bed(data, day):

    # Get sleep times in minutes
    bedtime, wake_up, _ = get_sleep_times(data, day)

    # Check if data is available
    if bedtime is None or wake_up is None:
        return None

    # Calculate total time in bed
    return wake_up - bedtime

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

if __name__ == "__main__":

    weekly_overview()
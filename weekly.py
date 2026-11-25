import add_Sleep_data


# Calculate sleep duration in minutes for a selected day
def calculate_sleep_duration(data, day):

    # Get sleep data for the selected day
    bedtime = data[day]["Bedtime"]
    wake_up = data[day]["Wake-up time"]
    fall_asleep = data[day]["Time to fall asleep"]

    # print(bedtime)
    # print(wake_up)
    # print(fall_asleep)

    # Check if data is available ( To prevent the program from throwing an error when generating a weekly report—for exam, in cases where the user has only filled in three out of the seven days)
    if bedtime is None or wake_up is None or fall_asleep is None:
        return None


    # Convert time to minutes
    bedtime_minutes = int(bedtime[0:2]) * 60 + int(bedtime[3:5])
    wake_up_minutes = int(wake_up[0:2]) * 60 + int(wake_up[3:5])
    fall_asleep_minutes = int(fall_asleep[0:2]) * 60 + int(fall_asleep[3:5])

    # print("Bedtime in minutes:", bedtime_minutes)
    # print("Wake-up time in minutes:", wake_up_minutes)
    # print("Time to fall asleep in minutes:", fall_asleep_minutes)

    # Handle sleep across midnight
    wake_up_minutes += 24 * 60

    print("Adjusted wake-up time:", wake_up_minutes)

    # Calculate actual sleep duration
    duration = wake_up_minutes - bedtime_minutes - fall_asleep_minutes
    print("Actual sleep duration:", duration)

    # Check if sleep duration is valid
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
    # Load saved sleep data from the JSON file from add_Sleep_data.py
    data_w = add_Sleep_data.load_data() 

    print(data_w)

    # Open the TXT file in write mode
    with open("weekly_data.txt", "w", newline="") as file:
    # Write the report title
        file.write("=== Weekly Sleep Report ===\n\n")

        # Write sleep data for each day
        for day in add_Sleep_data.days:
            file.write(f"{day}\n")

            for field, value in data_w[day].items():
                file.write(f"{field}: {value}\n")

            # Calculate sleep duration
            duration = calculate_sleep_duration(data_w, day)

            # Format sleep duration
            formatted_duration = format_sleep_duration(duration)

            # Write sleep duration to the report
            file.write(f"*** Sleep duration: {formatted_duration} ***\n")

            file.write("\n")

    print("Weekly report saved successfully!")


if __name__ == "__main__":

    weekly_overview()
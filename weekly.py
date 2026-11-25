import csv
import add_Sleep_data

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

        file.write("\n")

print("Weekly report saved successfully!")

# Calculate sleep duration in minutes
def calculate_sleep_duration(bedtime, wake_up, fall_asleep):

    # Check if all required data is available
    if bedtime is None or wake_up is None or fall_asleep is None:
        return None

    # Convert bedtime to minutes
    bedtime_minutes = int(bedtime[:2]) * 60 + int(bedtime[3:])

    # Convert wake-up time to minutes
    wake_up_minutes = int(wake_up[:2]) * 60 + int(wake_up[3:])

    # Convert time to fall asleep to minutes
    fall_asleep_minutes = int(fall_asleep[:2]) * 60 + int(fall_asleep[3:])

    # Handle sleep across midnight
    if wake_up_minutes < bedtime_minutes:
        wake_up_minutes += 24 * 60

    # Calculate actual sleep duration
    duration = wake_up_minutes - bedtime_minutes - fall_asleep_minutes

    return duration
   


if __name__ == "__main__":
        pass
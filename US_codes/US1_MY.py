from datetime import date

sleep_records = []

def record_sleep_minutes():
    while True:
        try:
            minutes = int(input("How many minutes did it take you to fall asleep? "))

            if minutes < 0:
                print("Minutes cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")

    today = date.today()
    record = (str(today), minutes)
    sleep_records.append(record)
    print("✅ Fall-asleep time saved.")

    print("You fell asleep in", minutes, "minutes.")
    print("Sleep records:", sleep_records)

    


record_sleep_minutes()
record_sleep_minutes()
record_sleep_minutes()
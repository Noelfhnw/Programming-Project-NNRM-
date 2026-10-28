from datetime import date


caffeine_records = []
alcohol_records = []

def caffeine_alcohol_consumption():
    while True:
        caffeine = input("Did you consume caffeine today? (yes/no): ").strip().lower()

        if caffeine not in ['yes', 'no']:
            print("Please answer 'yes' or 'no'.")
            continue
        break

    while True:
        alcohol = input("Did you consume alcohol today? (yes/no): ").strip().lower()

        if alcohol not in ['yes', 'no']:
            print("Please answer 'yes' or 'no'.")
            continue
        break

    today = date.today()
    record_caffeine = (str(today), "Caffeine: " + caffeine)
    record_alcohol = (str(today), "Alcohol: " + alcohol)

    caffeine_records.append(record_caffeine)
    alcohol_records.append(record_alcohol)
    print("✅ Caffeine and alcohol consumption saved.")


    print(caffeine_records)
    print(alcohol_records)
    
    return caffeine, alcohol

if __name__ == "__main__":
    caffeine_alcohol_consumption()
    caffeine_alcohol_consumption()
    caffeine_alcohol_consumption()

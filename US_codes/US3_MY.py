
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


                


caffeine_alcohol_consumption()

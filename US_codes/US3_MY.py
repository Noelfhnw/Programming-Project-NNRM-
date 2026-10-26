
def caffeine_alcohol_consumption():
    while True:
        consumption = input("Did you consume caffeine or alcohol today? (yes/no): ").strip().lower()

        if consumption not in ['yes', 'no']:
            print("Please answer  'yes' or 'no'.")
            continue
        else: 
            break

                


caffeine_alcohol_consumption()

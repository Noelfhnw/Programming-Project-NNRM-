#add sleep data file
#all inputs

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
fields = ["Bedtime", "Wake-up time", "Time to fall asleep", "Morning rating", "Caffeine_Alcohol consume"]


def create_data():
    data = {}
    
    for day in days:
        data [day] = {"Bedtime":None,"Wake-up time":None,"Time to fall asleep":None, "Morning rating":None, "Caffeine_Alcohol consume":None}
    return data



def show_data(data):
    for day in days:
        print(day)
        for field, value in data[day].items():
            print (f" {field} : {value}")



def menu_sleep_data(data):
    while True:
        print(""" 
=== Your Sleep Data ===

        """)
        show_data(data)

        print(""" 
  
What would you like to do?
1. Enter or change data
2. Back to main menu
    
                """)
        

        auswahl = input("choose an option: ")
        if auswahl == "1" :
            enter_data(data)
        elif auswahl == "2":
            break
        else:
            print("-------------------------------")
            print("")
            print("        !WRONG INPUT!")
            print("")
            print("-------------------------------")




def enter_data(data):
    print("""
=== Enter Sleep Data ===

For which day do you wannt to enter or change data?

1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday

    """)
    chosen_day = int(input("Choose a day (1-7): "))
    day = days[chosen_day -1]

    if chosen_day == 7:
        next_day ="Monday"
    else:
        next_day = days[chosen_day]

    while True:
        
        for field, value in data[day].items():
            print (f" {field} : {value}")

    
        print(f"""
=== Enter changing Data ===
    
Which value do you want to enter or change for {day}?
    
1. Bedtime
2. Wake-up time
3. Time to fall asleep
4. Morning rating
5. Caffeine_Alcohol consume
6. Go Back to overview
    
         """)
    
        chosen_field = int(input("Choose the data you want to log (1-6): "))
        if chosen_field == 6:
            break
        field = fields[chosen_field -1]
        print (f"""
=== Enter {field} of {day} ===

        """)


        if field == "Bedtime":
            bedtime_data = input(f"Type in the time you went to bed on {day} (HH:MM): ")
            data[day]["Bedtime"] = bedtime_data
        elif field == "Wake-up time":
            wake_up_data = input(f"When did you wake up on {next_day} (HH:MM): ")
            data[day]["Wake-up time"]= wake_up_data
        elif field == "Time to fall asleep":
            fall_asleep_data = input(f"How long did it take you to fall asleep on {day} (HH:MM): ")
            data[day]["Time to fall asleep"]= fall_asleep_data
        elif field == "Morning rating":
            morning_rating_data = int(input(f"How good to you feel after get up on {next_day} on a scale from (1-5) --> (1=miserable, 2=bad, 3=okay, 4=good, 5=very good): "))
            data[day]["Morning rating"]= morning_rating_data
        elif field == "Caffeine_Alcohol consume":
            caffeine_alcohol_data = input(f"Did you consume Caffeine or Alcohol after 2pm on {day} (yes/no): ").strip().lower()
            data[day]["Caffeine_Alcohol consume"]= caffeine_alcohol_data



data = create_data()
menu_sleep_data(data)



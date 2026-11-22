#add sleep data file
#all inputs

import json
import os

def save_data(data):
    with open ("sleep_data.json", "w") as file:
        json.dump(data, file)

def load_data():
    if os.path.exists("sleep_data.json"):
        with open ("sleep_data.json", "r") as file:
            return json.load(file)
    else:
        data = create_data()
        save_data(data)
        return data

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

For which day do you want to enter or change data?

1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday

    """)
    chosen_day =input("Choose a day (1-7): ")
    while not chosen_day.isdigit() or int(chosen_day) < 1 or int(chosen_day) > 7:
        print("-------------------------------")
        print("")
        print("        !WRONG INPUT!")
        print("")
        print("-------------------------------")
        chosen_day = input("Choose a day (1-7): ")

    chosen_day = int(chosen_day)

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
    
        chosen_field =input("Choose the data you want to log (1-6): ")
        while not chosen_field.isdigit() or int(chosen_field) < 1 or int(chosen_field) > 6:
            print("-------------------------------")
            print("")
            print("        !WRONG INPUT!")
            print("")
            print("-------------------------------")
            chosen_field = input("Choose the data you want to log (1-6): ")

        chosen_field = int(chosen_field)

        if chosen_field == 6:
            break
        field = fields[chosen_field -1]
        print (f"""
=== Enter {field} of {day} ===

        """)


        if field == "Bedtime":
            bedtime_data = input(f"Type in the time you went to bed on {day} (HH:MM): ")
            if len(bedtime_data) == 4:
                bedtime_data = "0" + bedtime_data
            while not time_input_valid_bedtime_data(bedtime_data):
                print("Invalid input! --> HH:MM format")
                bedtime_data = input(f"Type in the time you went to bed on {day} (HH:MM): ")
                if len(bedtime_data) == 4:
                    bedtime_data = "0" + bedtime_data
            data[day]["Bedtime"] = bedtime_data
            save_data(data)

        elif field == "Wake-up time":
            wake_up_data = input(f"When did you wake up on {next_day} (HH:MM): ")
            if len(wake_up_data) == 4:
                wake_up_data = "0" + wake_up_data
            while not time_input_valid_wake_up_data(wake_up_data):
                print("Invalid input! --> HH:MM format")
                wake_up_data = input(f"When did you wake up on {next_day} (HH:MM): ")
                if len(wake_up_data) == 4:
                    wake_up_data = "0" + wake_up_data
            data[day]["Wake-up time"]= wake_up_data
            save_data(data)

        elif field == "Time to fall asleep":
            fall_asleep_data = input(f"How long did it take you to fall asleep on {day} (HH:MM): ")
            if len(fall_asleep_data) == 4:
                fall_asleep_data = "0" + fall_asleep_data
            while not time_input_valid_fall_asleep_data(fall_asleep_data):
                print("Invalid input! --> HH:MM format")
                fall_asleep_data = input(f"How long did it take you to fall asleep on {day} (HH:MM): ")
                if len(fall_asleep_data) == 4:
                    fall_asleep_data = "0" + fall_asleep_data
            data[day]["Time to fall asleep"]= fall_asleep_data
            save_data(data)

        elif field == "Morning rating":
            morning_rating_data = input(f"How good do you feel after getting up on {next_day} on a scale from (1-5) --> (1=miserable, 2=bad, 3=okay, 4=good, 5=very good): ")
            while not input_valid_morning_rating(morning_rating_data):
                print("Invalid input! --> enter a number between 1-5")
                morning_rating_data = input(f"How good do you feel after getting up on {next_day} on a scale from (1-5) --> (1=miserable, 2=bad, 3=okay, 4=good, 5=very good): ")
            data[day]["Morning rating"]= morning_rating_data
            save_data(data)

        elif field == "Caffeine_Alcohol consume":
            caffeine_alcohol_data = input(f"Did you consume Caffeine or Alcohol after 2pm on {day} (yes/no): ").strip().lower()
            while not input_valid_caffeine_alcohol_data(caffeine_alcohol_data):
                print("Invalid input! --> enter yes or no")
                caffeine_alcohol_data = input(f"Did you consume Caffeine or Alcohol after 2pm on {day} (yes/no): ").strip().lower()
            data[day]["Caffeine_Alcohol consume"]= caffeine_alcohol_data
            save_data(data)


def time_input_valid_bedtime_data(bedtime_data):
    if len(bedtime_data) != 5:
        return False
    elif bedtime_data[2] != ":":
        return False
    hours_text = bedtime_data[0:2]
    minutes_text = bedtime_data[3:5]
    if not hours_text.isdigit() or not minutes_text.isdigit():
        return False
    hours = int(hours_text)
    minutes = int(minutes_text)
    if hours >= 24 or hours < 0:
        return False
    if minutes >= 60 or minutes < 0:
        return False
    return True

def time_input_valid_wake_up_data(wake_up_data):
    if len(wake_up_data) != 5:
        return False
    elif wake_up_data[2] != ":":
        return False
    hours_text = wake_up_data[0:2]
    minutes_text = wake_up_data[3:5]
    if not hours_text.isdigit() or not minutes_text.isdigit():
        return False
    hours = int(hours_text)
    minutes = int(minutes_text)
    if hours >= 24 or hours < 0:
        return False
    if minutes >= 60 or minutes < 0:
        return False
    return True

def time_input_valid_fall_asleep_data(fall_asleep_data):
    if len(fall_asleep_data) != 5:
        return False
    elif fall_asleep_data[2] != ":":
        return False
    hours_text = fall_asleep_data[0:2]
    minutes_text = fall_asleep_data[3:5]
    if not hours_text.isdigit() or not minutes_text.isdigit():
        return False
    hours = int(hours_text)
    minutes = int(minutes_text)
    if hours >= 24 or hours < 0:
        return False
    if minutes >= 60 or minutes < 0:
        return False
    return True

def input_valid_morning_rating(morning_rating_data):
    if len(morning_rating_data) != 1:
        return False
    morning_rating_text = morning_rating_data
    if not morning_rating_text.isdigit():
        return False
    morning_rating = int(morning_rating_text)
    if morning_rating > 5 or morning_rating < 1:
        return False
    return True

def input_valid_caffeine_alcohol_data(caffeine_alcohol_data):
    if caffeine_alcohol_data != "yes" and caffeine_alcohol_data != "no":
        return False
    return True

data = load_data()
menu_sleep_data(data)



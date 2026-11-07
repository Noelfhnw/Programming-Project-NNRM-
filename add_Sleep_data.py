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

    print(f"""
=== Enter changing Data ===
    
Which value do you want to enter or change for {day}?
    
1. Bedtime
2. Wake-up time
3. Time to fall asleep
4. Morning rating
5. Caffeine_Alcohol consume
    
        """)
    
    chosen_field = int(input("Choose the data you want to log (1-5): "))
    field = fields[chosen_field -1]
    print (field)

data = create_data()
menu_sleep_data(data)



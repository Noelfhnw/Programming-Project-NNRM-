import add_Sleep_data
import daily
import weekly

def show_menu():
    print("""
MENU
---Sleep tracker---
1. Add sleep data


---View sleep analysis and recommendations---
2. Daily
3. Weekly


---Close application---
4. Exit
""")


def add_sleep_data_Main():
    data = add_Sleep_data.load_data()
    add_Sleep_data.menu_sleep_data(data)

def daily_Main():
    daily.daily()

def weekly_Main():
    weekly.weekly()
        

def main():
    while True:
        show_menu()
        auswahl = input("choose an option: ")
        if auswahl == "1" :
            add_sleep_data_Main()
        elif auswahl == "2":
            daily_Main()
        elif auswahl == "3":
            weekly_Main()
        elif auswahl == "4":
            break
        else:
            print("-------------------------------")
            print("")
            print("        !WRONG INPUT!")
            print("")
            print("-------------------------------")

main()
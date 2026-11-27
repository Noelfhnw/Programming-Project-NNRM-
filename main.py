import add_Sleep_data
import daily

def show_menu():
    print("MENU")
    print()
    print("---Sleep Diary--------------------------------")
    print("1. Add sleep data")
    print()
    print("---View sleep analysis and recommendations----")
    print("2. Daily")
    print("3. Weekly")
    print()
    print("----------------------------------------------")
    print("4. Exit")


def add_sleep_data_Main():
    data = add_Sleep_data.load_data()
    add_Sleep_data.menu_sleep_data(data)

def daily_Main():
    daily.daily()

def weekly_Main():
    print("TO DO weekly")
        

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
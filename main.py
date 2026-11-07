#Input:
    #- US1: Time to fall asleep
    #- US3: Caffeine & Alcohol Consume
    #- US4: Bed- & Wake-up- time 
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


def add_sleep_data():
    print("TO DO add_slee_data")

def daily():
    print("TO DO daily")

def weekly():
    print("TO DO weekly")
        

def main():
    while True:
        show_menu()
        auswahl = input("choose an option: ")
        if auswahl == "1" :
            add_sleep_data()
        elif auswahl == "2":
            daily()
        elif auswahl == "3":
            weekly()
        elif auswahl == "4":
            break
        else:
            print("-------------------------------")
            print("")
            print("        !WRONG INPUT!")
            print("")
            print("-------------------------------")

main()
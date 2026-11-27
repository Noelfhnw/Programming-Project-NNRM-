import add_Sleep_data
from datetime import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = datetime.now()
daily_weekday = now.isoweekday()-2

days_for_average_wakeup = days

day_d = days[daily_weekday]


import os


#print(daily_weekday)
#-------------------------------------------ÄNDER VOR GEBRAUCH AKTUELL TEST DICT---------------------------------------------------------------------------

data_d = add_Sleep_data.load_data()
#data_d = 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #print(day_d)   = Todaysweekday -1
    #print(data_d[day_d]) = the dict. of yesterday
    #print(data_d[day_d]["Wake-up time"]) = the specific data of yesterday
    #fields = ["Bedtime", "Wake-up time", "Time to fall asleep", "Morning rating", "Caffeine_Alcohol consume"]

#-------------------------------------DAILY DATA------------------------------------------------------

def sleep_time():
    bedtime_d = data_d[day_d]["Bedtime"]
    wake_up_time_d = data_d[day_d]["Wake-up time"]
    hours_bedtime_d, minutes_bedtime_d = bedtime_d.split(":")
    hours_wakeup_d, minutes_wakeup_d = wake_up_time_d.split(":")
    bedtime_in_minutes = int(hours_bedtime_d) * 60 + int(minutes_bedtime_d) + int(data_d[day_d]["Minutes to fall asleep"])
    wakeuptime_in_minutes = int(hours_wakeup_d) * 60 + int(minutes_wakeup_d)
    sleepduration_in_minutes = wakeuptime_in_minutes - bedtime_in_minutes
    if sleepduration_in_minutes < 0:
        sleepduration_in_minutes += 24*60
    if sleepduration_in_minutes == 0:
        return("Please check Input!")
    else:
        return(f"{sleepduration_in_minutes // 60}h {sleepduration_in_minutes % 60}min")

def caffeine_alcohol_Y_N_forData():
    caffeine_alcohol = data_d[day_d]["Caffeine_Alcohol consume"]
    if caffeine_alcohol == "yes":
        return("Yesterday you consumed caffeine or alcohol after 2pm!")
    elif caffeine_alcohol == "no":
        return("Yesterday you did not consume caffeine or alcohol after 2pm!")
    else:
        return("Please check Input!")

#(1=miserable, 2=bad, 3=okay, 4=good, 5=very good)
def morning_rating_forData():
    morning_rating_d_Data = data_d[day_d]["Morning rating"]
    if morning_rating_d_Data == 1:
        return("You woke up feeling miserable (1) this morning. Hopefully tonight brings better rest!")
    elif morning_rating_d_Data == 2:
        return("You woke up feeling bad (2) this morning. Your sleep could use some improvement.")
    elif morning_rating_d_Data == 3:
        return("You woke up feeling okay (3) this morning. Not bad, but there's room for improvement")
    elif morning_rating_d_Data == 4:
        return("You woke up feeling good (4) this morning. Nice, your sleep did its job!")
    elif morning_rating_d_Data == 5:
        return("You woke up feeling very good (5) this morning. Fantastic, keep up this routine!")
    else:
        return("Please check Input!")

#-----------------------------RECOMMENDATION-------------------------------------------------------------------

def caffeine_alcohol_Y_N_forRecomendation():
    caffeine_alcohol = data_d[day_d]["Caffeine_Alcohol consume"] #mit Noel anschauen bez. Input von Data (TRUE/FALSE)
    if caffeine_alcohol == "yes":
        return("Tip: Try not to consume caffeine or alcohol after 2pm... it improves your sleep!")
    elif caffeine_alcohol == "no":
        return("Great! You did not consume any caffeine or alcohol after 2pm... your body thanks you!")
    else:
        return("Please check Input!")

def weekly_consitency():
    wake_up_times_allDays = []
    for entry in data_d.values():
        if entry ["Wake-up time"] is not None:
            wake_up_times_allDays.append(time_to_minutes_d(entry["Wake-up time"]))
    if len(wake_up_times_allDays)>=4:
        average_wake_up = round(sum(wake_up_times_allDays) / len(wake_up_times_allDays))
        average_wake_up_hour = average_wake_up // 60 
        average_wake_up_minute = average_wake_up % 60

        ideal_bedtime = average_wake_up - 8 * 60
        if ideal_bedtime < 0:
            ideal_bedtime += 24 * 60
        ideal_bedtime_hour = ideal_bedtime // 60
        ideal_bedtime_minute = ideal_bedtime % 60

        return(f"Your average wake up time is {average_wake_up_hour:02d}:{average_wake_up_minute:02d}. "
               f"Try to go to sleep by {ideal_bedtime_hour:02d}:{ideal_bedtime_minute:02d}. So that you sleep 8h!")
    else:
        return(f"Weekly Average: Not enough Data yet! You have {len(wake_up_times_allDays)} of 4 nights logged.")

def time_to_minutes_d(Time):
    hours_string, minutes_string = Time.split(":")
    hours_int = int(hours_string)*60
    minutes_int = int(minutes_string)
    return hours_int + minutes_int

def training_readiness():
    score = sleep_score()
    if score is None:
        return None
    if score >= 75:
        return("Today you are ready for a hard workout. Your body is well rested, so make it count!")
    elif score >= 50:
        return("Today an easy workout is the right choice. Keep it light and listen to your body.")
    else: 
        return("Today is a good day to rest. Recover well, and your next workout will be stronger!")

#-----------------------------------SLEEP SCORE----------------------------------------------------------------

def duration_points():
    bedtime_d = data_d[day_d]["Bedtime"]
    wake_up_time_d = data_d[day_d]["Wake-up time"]
    hours_bedtime_d, minutes_bedtime_d = bedtime_d.split(":")
    hours_wakeup_d, minutes_wakeup_d = wake_up_time_d.split(":")
    bedtime_in_minutes = int(hours_bedtime_d) * 60 + int(minutes_bedtime_d) + int(data_d[day_d]["Minutes to fall asleep"])
    wakeuptime_in_minutes = int(hours_wakeup_d) * 60 + int(minutes_wakeup_d)
    sleepduration_in_minutes = wakeuptime_in_minutes - bedtime_in_minutes
    if sleepduration_in_minutes < 0:
        sleepduration_in_minutes += 24*60
    missing = max(0, 480 - sleepduration_in_minutes)
    steps = missing // 30
    points_deducted = steps * 5
    points_duration = max(0, 50 - points_deducted)
    return(points_duration)

def morning_rating_points():
    rating = int(data_d[day_d]["Morning rating"])
    if rating is None:
        return None
    result = rating * 5
    return(result)

def caffeine_alcohol_points():
    caffeine_alcohol = data_d[day_d]["Caffeine_Alcohol consume"]
    if  caffeine_alcohol == "no":
        points = 25
    elif caffeine_alcohol == "yes":
        points = 0
    else:
        return None
    return(points)

def sleep_score():
    duration = duration_points()
    rating = morning_rating_points()
    habits = caffeine_alcohol_points()
    if rating is None or habits is None:
        return None
    return duration + rating + habits

#------------------------------------------TXT FILE-----------------------------------------------------------

def next_file():
    number = 1
    while os.path.exists(f"exports/daily_{number:03d}.txt"):
        number += 1
    return f"exports/daily_{number:03d}.txt"

def export_daily():
    os.makedirs("exports", exist_ok=True)
    filename = next_file()
    with open(filename, "w", encoding="utf-8") as file:
        file.write(daily_text())
    print(f"Exported to {filename}")

def daily_text():
    lines = []
    lines.append(f"---Daily sleep review for {day_d} night---------------------------------------------------")
    lines.append("")
    lines.append("---Sleep summary:---")
    lines.append("")
    lines.append(f"You went to bed by: {data_d[day_d]['Bedtime']}")
    lines.append(f"You woke up at: {data_d[day_d]['Wake-up time']}")
    lines.append(f"It took you {data_d[day_d]['Minutes to fall asleep']} minutes to fall asleep")
    lines.append(f"That puts your total sleep duration to: {sleep_time()}")
    lines.append(caffeine_alcohol_Y_N_forData())
    lines.append(morning_rating_forData())
    lines.append("")
    lines.append(f"---Sleep score for {day_d} night:---")
    lines.append("")
    lines.append(f"Your sleep score is {sleep_score()}/100")
    lines.append(f"Sleep duration from 8h: {duration_points()}/50")
    lines.append(f"Morning rating: {morning_rating_points()}/25")
    lines.append(f"Caffeine and alcohol consumption: {caffeine_alcohol_points()}/25")
    lines.append("")
    lines.append("---Recommendation:---")
    lines.append("")
    lines.append(training_readiness())
    lines.append(weekly_consitency())
    lines.append(caffeine_alcohol_Y_N_forRecomendation())
    return "\n".join(lines)   

#------------------------------------------FRONT MENU---------------------------------------------------------  

def daily():
    global data_d
    global day_d

    data_d = add_Sleep_data.load_data()

    now = datetime.now()
    daily_weekday = now.isoweekday() - 2
    day_d = days[daily_weekday]

    missing_fields = []
    for field, value in data_d[day_d].items():
        if value is None:
            missing_fields.append(field)

    if len(missing_fields) > 0:
        print(f"Data for {day_d} night is incomplete!")
        print("Missing:")
        for field in missing_fields:
            print(f" - {field}")
        exit_to_main_menu()
        return
    print(f"---Daily sleep review for {day_d} night---------------------------------------------------")
    print("")
    print("---Sleep summary:---")
    print("")
    print(f"You went to bed by: {data_d[day_d]["Bedtime"]}")
    print(f"You woke up at: {data_d[day_d]["Wake-up time"]}")
    print(f"It took you {data_d[day_d]["Minutes to fall asleep"]} minutes to fall asleep")
    print(f"That puts your total sleep duration to: {sleep_time()}")
    print(f"{caffeine_alcohol_Y_N_forData()}")
    print(f"{morning_rating_forData()}")
    print("")
    print(f"---Sleep score for {day_d} night:---")
    print("")
    print(f"Your sleep score is {sleep_score()}/100")
    print(f"Sleep duration from 8h: {duration_points()}/50")
    print(f"Morning rating: {morning_rating_points()}/25")
    print(f"Caffeine and alcohol consumption: {caffeine_alcohol_points()}/25")
    print("")
    print(f"---Recommendation:---")
    print("")
    print(f"{training_readiness()}")
    print(f"{weekly_consitency()}")
    print(f"{caffeine_alcohol_Y_N_forRecomendation()}")
    exit_to_main_menu()

def exit_to_main_menu():
    while True:
        print()
        print("---------------------------------------------------------------------------------------")
        print("")
        print("1. Export to text file")
        print("2. Exit to main menu")
        choice = input("choose an option: ")
        if choice == "1":
            export_daily()
        elif choice == "2":
            break
        else:
            print("-------------------------------")
            print("")
            print("        !WRONG INPUT!")
            print("")
            print("-------------------------------")

#--------------------------------------------TEST ZONE-------------------------------------------------------------


#endziel wäre eine schlafzeit von 10h mit diesen angaben
bedtime_d = "20:30" #1230min
wake_up_time_d = "06:30" #390min
hours_bedtime_d, minutes_bedtime_d = bedtime_d.split(":")
hours_wakeup_d, minutes_wakeup_d = wake_up_time_d.split(":")
bedtime_in_minutes = int(hours_bedtime_d) * 60 + int(minutes_bedtime_d) - 15
wakeuptime_in_minutes = int(hours_wakeup_d) * 60 + int(minutes_wakeup_d)
sleepduration_in_minutes = wakeuptime_in_minutes - bedtime_in_minutes
if sleepduration_in_minutes < 0:
    sleepduration_in_minutes += 24*60
#if sleepduration_in_minutes == 0:
#    print("Please check Input!")
#else:
#    print(f"{sleepduration_in_minutes // 60}h {sleepduration_in_minutes % 60}min")

import add_Sleep_data
from datetime import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = datetime.now()
daily_weekday = now.isoweekday()-2

for i in range(1, 5):
    index = (daily_weekday)

days_for_average_wakeup = days

day_d = days[daily_weekday]

#print(daily_weekday)

data_d = add_Sleep_data.create_data()

    #print(day_d)   = Todaysweekday -1
    #print(data_d[day_d]) = the dict. of yesterday
    #print(data_d[day_d]["Wake-up time"]) = the specific data of yesterday
    #fields = ["Bedtime", "Wake-up time", "Time to fall asleep", "Morning rating", "Caffeine_Alcohol consume"]

def sleep_time():
    bedtime_d = data_d[day_d]["Bedtime"]
    wake_up_time_d = data_d[day_d]["Wake-up time"]
    hours_bedtime_d, minutes_bedtime_d = bedtime_d.split(":")
    hours_wakeup_d, minutes_wakeup_d = wake_up_time_d.split(":")
    bedtime_in_minutes = int(hours_bedtime_d) * 60 + int(minutes_bedtime_d) - int(data_d[day_d]["Time to fall asleep"])
    wakeuptime_in_minutes = int(hours_wakeup_d) * 60 + int(minutes_wakeup_d)
    sleepduration_in_minutes = wakeuptime_in_minutes - bedtime_in_minutes
    if sleepduration_in_minutes < 0:
        sleepduration_in_minutes += 24*60
    if sleepduration_in_minutes == 0:
        print("Please check Input!")
    else:
        print(f"{sleepduration_in_minutes // 60}h {sleepduration_in_minutes % 60}min")

def caffeine_alcohol_Y_N_forRecomendation():
    caffeine_alcohol = data_d[day_d]["Caffeine_Alcohol consume"] #mit Noel anschauen bez. Input von Data (TRUE/FALSE)
    if caffeine_alcohol == "yes":
        print("Tip: Try not to consume caffeine or alcohol after 2pm... it improves your sleep!")
    if caffeine_alcohol == "no":
        print("Great! You did not consume any caffeine or alcohol after 2pm... your body thanks you!")
    else:
        print("Please check Input!")

def caffeine_alcohol_Y_N_forData():
    caffeine_alcohol = data_d[day_d]["Caffeine_Alcohol consume"]
    if caffeine_alcohol == "yes":
        print("Yesterday you consumed caffeine or alcohol after 2pm!")
    if caffeine_alcohol == "no":
        print("Yesterday you did not consume caffeine or alcohol after 2pm!")
    else:
        print("Please check Input!")

#(1=miserable, 2=bad, 3=okay, 4=good, 5=very good)
def morning_rating_forData():
    morning_rating_d_Data = data_d[day_d]["Morning rating"]
    if morning_rating_d_Data == 1:
        print("You woke up feeling miserable (1) this morning. Hopefully tonight brings better rest!")
    elif morning_rating_d_Data == 2:
        print("You woke up feeling bad (2) this morning. Your sleep could use some improvement.")
    elif morning_rating_d_Data == 3:
        print("You woke up feeling okay (3) this morning. Not bad, but there's room for improvement")
    elif morning_rating_d_Data == 4:
        print("You woke up feeling good (4) this morning. Nice, your sleep did its job!")
    elif morning_rating_d_Data == 5:
        print("You woke up feeling very good (5) this morning. Fantastic, keep up this routine!")
    else:
        print("Please check Input!")

def weekly_consitency():
    wake_up_time_d = data_d[day_d]["Wake-up time"]

def sleep_score():
    print()

def daily():
    print(f"---Daily sleep review for {day_d} night---------------------------------------------------")
    print("")
    print("Sleep summary:")
    print(f"You went to bed by: {data_d[day_d]["Bedtime"]}")
    print(f"You woke up at: {data_d[day_d]["Wake-up time"]}")
    print(f"It took you {data_d[day_d]["Time to fall asleep"]} minutes to fall asleep")
    print(f"That puts your total sleep duration to: {sleep_time}")
    print(f"{caffeine_alcohol_Y_N_forData}")
    print(f"{morning_rating_forData}")
    print(f"---Sleep Score for {day_d} night-----------------------------------------------------------")


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
if sleepduration_in_minutes == 0:
    print("Please check Input!")
else:
    print(f"{sleepduration_in_minutes // 60}h {sleepduration_in_minutes % 60}min")


daily()
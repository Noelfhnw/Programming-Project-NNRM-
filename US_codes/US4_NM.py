## US-04: Log bedtime and wake-up time
#**Assigned to:** 
#
#As a user, I want to log my bedtime and wake-up time, so that the program knows how long I slept.

#**Acceptance criteria**
#- [ ] The program asks for bedtime and wake-up time. The date is today's date.
#- [ ] Given the input `25:00` or `7pm` as time, then `⚠️ Invalid time. Use HH:MM.` is displayed and the question is asked again.
#- [ ] Given bedtime `23:30` and wake-up `07:00`, then the night is saved with a duration of 7h 30min.
#- [ ] After saving, `✅ Night saved.` is displayed. If `sleep_log.csv` does not exist, it is created automatically.
#- [ ] In none of the invalid cases does the program crash (no Python traceback).

from US1_MY.py import record sleep minutes

def bed_wake-up_time():
    bedtime = input("When did you go to bed last night? (HH:MM)".strip)
        if len(bedtime) != 4:
            print("⚠️ Invalid time. Use HH:MM")

        if 


    wakeuptime = input("When did you wake up today? (HH:MM)".strip)
        if len(wakeuptime) != 4:
            print("⚠️ Invalid time. Use HH:MM")


# --> wie Daten für ganze Woche aufnehmen und speichern
from US3_MY import caffeine_alcohol_consumption

caffeine, alcohol = caffeine_alcohol_consumption()

print("Caffeine:", caffeine)
print("Alcohol:", alcohol)

def give_sleep_tips():

    if caffeine == "yes":
        print("☕ Avoid caffeine after 14:00")

    if alcohol == "yes":
        print("🍷 Avoid alcohol in the 3 hours before bedtime.")   

    if caffeine == "no" and alcohol == "no":
        print("✅ No caffeine or alcohol logged. Keep it up!")     


give_sleep_tips()
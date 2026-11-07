#add sleep data file
#all inputs

print("")


tage = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daten = {}

for tag in tage:
    daten [tag] = {"Bedtime":None,"Wake-up time":None,"time to fall asleep":None, "Morning rating":None, "Caffeine_Alcohol consume":None}
for tag in tage:
    print(tag)
    for eingabe, wert in daten[tag].items():
        print (f" {eingabe} : {wert}")
    



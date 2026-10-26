minutes = int(input("How many minutes did it take you to fall asleep? "))
while minutes < 0 :
    minutes = int(input("Please enter valid minutes: "))

print("You fell asleep in", minutes, "minutes.")
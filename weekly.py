import csv
import add_Sleep_data

# Load saved sleep data from the JSON file from add_Sleep_data.py
data_w = add_Sleep_data.load_data() 

print(data_w)
with open("weekly_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write column headers
    writer.writerow(["Day"] + add_Sleep_data.fields)

    # Write sleep data for each day
    for day in days:
        writer.writerow([day] + list(data_w[day].values()))


    if __name__ == "__main__":
        pass
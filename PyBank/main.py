import csv
import os

pybank_csv = os.path.join( 'budget_data.csv')

months = 0
total = 0
previous = 0
change = 0
totalchange=0
increase=0
decrease=0
increasemonth=""
decreasemonth=""
average=0

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

with open(pybank_csv) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    

    for row in csvreader:

        months += 1
        total += int(row["Profit/Losses"])

        if months > 1:
            change = int(row["Profit/Losses"]) - previous
            totalchange += change
            previous = int(row["Profit/Losses"])
        if change > increase:
            increase = change
            increasemonth=row["Date"]
        if change < decrease: 
            decrease = change
            decreasemonth=row["Date"]

    average=round(totalchange / (months-1),2)


print(f" \n")
print(f"Financial Analysis\n")
print(f"------------------------\n")
print(f"Total Months: {months}\n")
print(f"Total: ${total}\n")
print(f"Average Change: {average}\n")
print(f"Greatest Increase in Profits: {increasemonth} (${increase})\n")
print(f"Greatest Decrease in Profits: {decreasemonth} (${decrease})\n")


with open("pybank_output.txt", "w") as text_file:
    text_file.write(f" \n")
    text_file.write(f" \n")
    text_file.write(f"Financial Analysis\n")
    text_file.write(f"------------------------\n")
    text_file.write(f"Total Months: {months}\n")
    text_file.write(f"Total: ${total}\n")
    text_file.write(f"Average Change: {average}\n")
    text_file.write(f"Greatest Increase in Profits: {increasemonth} (${increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {decreasemonth} (${decrease})\n")
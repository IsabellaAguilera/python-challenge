import csv
import os

pypoll_csv = os.path.join('election_data.csv')

votes = 0
candidates = []
khan = 0
correy = 0
li = 0
otooley = 0
khanpercent = 0
correypercent = 0
lipercent = 0
otooleypercent = 0
winnder = 0

with open(pypoll_csv,newline='') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')

    for row in csvreader:

        votes += 1

        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"])

        if (row["Candidate"] == "Khan"):
            khan += 1
        elif (row["Candidate"] == "Correy"):
            correy += 1
        elif (row["Candidate"] == "Li"):
            li += 1
        else:
            otooley += 1

        if khan > correy or li or otooley:
            winner = "Khan"
        elif correy > li or khan or otooley:
            winner = "Correy"
        elif li > khan or correy or otooley:
            winner = "Li"
        else:
             winner = "O'Tooley"

    khanpercent = round((khan / votes) *100,3)
    correypercent = round((correy/votes) *100,3)
    lipercent = round((li/votes) *100,3)
    otooleypercent = round((otooley/votes) *100,3)
    


print(f"\n")
print(f"Election Results")
print(f"--------------------")
print(f"Total Votes: {votes}")
print(f"--------------------")
print(f"Khan: {khanpercent}% ({khan})")
print(f"Correy: {correypercent}% ({correy})")
print(f"Li: {lipercent}% ({li})")
print(f"O'Tooley: {otooleypercent}% ({otooley})")
print(f"--------------------")
print(f"Winner: {winner}")
print(f"--------------------")


with open("pypoll_output.txt","w") as text_file:
    text_file.write(f"\n")
    text_file.write(f"Election Results\n")
    text_file.write(f"--------------------\n")
    text_file.write(f"Total Votes: {votes}\n")
    text_file.write(f"--------------------\n")
    text_file.write(f"Khan: {khanpercent}% ({khan})\n")
    text_file.write(f"Correy: {correypercent}% ({correy})\n")
    text_file.write(f"Li: {lipercent}% ({li})\n")
    text_file.write(f"O'Tooley: {otooleypercent}% ({otooley})\n")
    text_file.write(f"--------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write(f"--------------------\n")
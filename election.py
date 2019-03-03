import os
import csv

election_csv = os.path.join("election_data.csv")

total = 0
nameArray = []
khanArray = []
correyArray = []
liArray = []
otooleyArray = []


with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:

        total = total + 1
        nameArray.append(str(row[2]))

        if row[2] == "Khan":
            khanArray.append(str(row[2]))
        if row[2] == "Correy":
            correyArray.append(str(row[2]))
        if row[2] == "Li":
            liArray.append(str(row[2]))
        if row[2] == "O'Tooley":
            otooleyArray.append(str(row[2]))


    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {total}")
    print(f"----------------------------")
    print(f"Khan: {round(((len(khanArray)/len(nameArray))*100),3)}% ({len(khanArray)})")
    print(f"Correy: {round(((len(correyArray)/len(nameArray))*100),3)}% ({len(correyArray)})")
    print(f"Li: {round(((len(liArray)/len(nameArray))*100),3)}% ({len(liArray)})")
    print(f"O'Tooley: {round(((len(otooleyArray)/len(nameArray))*100),3)}% ({len(otooleyArray)})")
    print(f"----------------------------")
    print(f"Winner: {max(set(nameArray), key=nameArray.count)}")
    print(f"----------------------------")


with open('electionTextFile.txt', 'w') as electionTextFile:
    print(f"Election Results", file=electionTextFile)
    print(f"----------------------------", file=electionTextFile)
    print(f"Total Votes: {total}", file=electionTextFile)
    print(f"----------------------------", file=electionTextFile)
    print(f"Khan: {round(((len(khanArray)/len(nameArray))*100),3)}% ({len(khanArray)})", file=electionTextFile)
    print(f"Correy: {round(((len(correyArray)/len(nameArray))*100),3)}% ({len(correyArray)})", file=electionTextFile)
    print(f"Li: {round(((len(liArray)/len(nameArray))*100),3)}% ({len(liArray)})", file=electionTextFile)
    print(f"O'Tooley: {round(((len(otooleyArray)/len(nameArray))*100),3)}% ({len(otooleyArray)})", file=electionTextFile)
    print(f"----------------------------", file=electionTextFile)
    print(f"Winner: {max(set(nameArray), key=nameArray.count)}", file=electionTextFile)
    print(f"----------------------------", file=electionTextFile)

            
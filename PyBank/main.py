import os
import csv

budget_csv = os.path.join("budget_data.csv")

count = 0
total = 0
diff = 0
totalArray = []
dateArray =[]
diffArray = []


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:

        count = count + 1
        total = total + int(row[1])
        totalArray.append(int(row[1]))
        dateArray.append(str(row[0]))
    
    for i in range(1, count):
        diffArray.append(totalArray[i] - totalArray[i-1])


    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round((sum(diffArray)/(count-1)),2)}")

    print(f"Greatest Increase in Profits: {dateArray[diffArray.index(max(diffArray))+1]} (${max(diffArray)})")
    print(f"Greatest Decrease in Profits: {dateArray[diffArray.index(min(diffArray))+1]} (${min(diffArray)})")

  
with open('budgetData.txt', 'w') as budgetData:
    print(f"Financial Analysis", file=budgetData)
    print(f"----------------------------", file=budgetData)
    print(f"Total Months: {count}", file=budgetData)
    print(f"Total: ${total}", file=budgetData)
    print(f"Average Change: ${round((sum(diffArray)/(count-1)),2)}", file=budgetData)

    print(f"Greatest Increase in Profits: {dateArray[diffArray.index(max(diffArray))+1]} (${max(diffArray)})", file=budgetData)
    print(f"Greatest Decrease in Profits: {dateArray[diffArray.index(min(diffArray))+1]} (${min(diffArray)})", file=budgetData)
    

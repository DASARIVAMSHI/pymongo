import csv
with open("week2.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        with open('week2.csv', 'r', newline="")as input, open('week.csv', 'w', newline="")as output:
            reader = csv.reader(input)
            writer = csv.writer(output)
            headerrow = next(reader)
            headerrow.append("totalpercentage")
            writer.writerow(headerrow)
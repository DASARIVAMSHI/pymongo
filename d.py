import csv
with open("Attendance.csv","r") as csvfile:
 reader = csv.reader(csvfile)
 for row in reader:
     print(row)
with open("Attendance.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    name=input("enter your name:-\n")
    id=input("enter id:-\n")
    for row in reader:
        if ((name.strip()==row[1])and(id.strip()==row[0])):
              print(row)
with open('Attendance.csv','r',newline="")as input,open('Attendancenew.csv','w',newline="")as output:
    reader = csv.reader(input)
    writer = csv.writer(output)
    headerrow = next(reader)
    headerrow.append("totalpercentage")
    writer.writerow(headerrow)
    for row in reader:
        totalpercentage = float(row[7])*100/float(row[6])
        row.append(totalpercentage)
        writer.writerow(row)
with open ("Attendancenew.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    print("students with less than 60% attendance:-")
    for row in reader:
        if(float(row[9])<60):
            print(row[1])

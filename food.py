import csv

#excel File Creation
fh=open("inventorySystem.csv","w+",newline="")
w=csv.writer(fh)

#Excel File Column Name
header=["Friuts Name","Unit Price","Quantity","Total Price"]
w.writerow(header)
data=[]

#Take item data from the user
while True:
    try:
        n=int(input("How Many insert Foods Records : "))
    except ValueError:
        print("Friuts Record are Number Please Again Entered")
        continue
    else:
        break

for i in range(n):
    print("Enter Fruit Record {0}:",i+1)
    fruitsName=input("Enter Fruits Name :")
    while True:
        try:
            unitPrice=float(input("Enter Unit Price :"))
        except ValueError:
            print("Enter Unit Price Please Try Again")
        else:
            break
    while True:
        try:
            quantity=int(input("Enter Quantity :"))
        except ValueError:
            print("Invalid Quantity Please Try Again")
        else:
            break
    totalPrice=unitPrice*quantity;

    #Store data in CSV(Excel)
    rec=[fruitsName,unitPrice,quantity,totalPrice]
    data.append(rec)
w.writerows(data)
fh.close()

#print summary
print("Print Fruits Items Summay Data From CSV")
fh=open("inventorySystem.csv","r")
r=csv.reader(fh)
for i in r:
    print(i)
fh.close()
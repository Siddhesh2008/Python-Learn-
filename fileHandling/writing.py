#Python writing files (.txt,.json,.csv)
import json
import csv
employees=[["name","age","job"],["John",30,"Manager"],["Jane",25,"Developer"],["Bob",35,"Tester"]]
file_path = "C:\\Users\\Siddhesh\\Desktop\\output.txt"

try:
    with open(file_path, "w") as file:   #w=write, a=append ,x=create, r=read
       writer=csv.writer(file)
       for row in employees:
           writer.writerow(row)
    print("File written successfully")
except FileExistsError:
    print("File already exists")
except:
    print("Something went wrong")
#Python reading files

file_path="C:\\Users\\Siddhesh\\Desktop\\output.txt"
try:
    with open(file_path,"r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
except:
    print("Something went wrong")
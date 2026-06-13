num=5
a=6
b=7
age=22
temp=30
user_role="admin"

print("positive" if num>0 else "negative")
result="EVEN"if  num%2==0 else "ODD"
print(result)
max_num=a if a>b else b
print("the maximum number is",max_num)
min_num=a if a<b else b
print("the minimum number is",min_num)
status= "Adult" if age >=18 else "Minor"
print("the person is an",status)
weather= "HOT" if temp>=20 else "COLD"
print("the weather is",weather)
access_level= "Full Access" if user_role=="admin" else "Limited Access"
print("the user has",access_level)

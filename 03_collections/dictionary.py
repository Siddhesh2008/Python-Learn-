#dictionary={key:values},no duplicates

capitals={"USA":"washington",
"India":"New Delhi",
"China":"Beijing",
"Russia":"Moscow"}

#print(dir(capitals))
#print(help(capitals))
print(capitals.get("USA"))       #fetches the value of the key USA

capitals.update({"germany":"berlin"}) #to insert or update
capitals.update({"USA":"Washington D.C"})
capitals.pop("China")     #removes
capitals.popitem()      #removes the lastest value
#capitals.clear()       #clears

print(capitals.keys())     #to return the keys

for key in capitals.keys():
    print(key,end=" ")      #the same goes for values tooo
                            #capitals.values
print()

for key,value in capitals.items():
    print(f"{key}:{value}",end=" ")
print()





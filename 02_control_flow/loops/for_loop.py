for x in  reversed(range(1,11)):
    print(x)
print("Happy new year")

for x in range(1,21):
    if x==13:
        continue        ##skips 13
    else:
        print(x)

for x in range(1,21):
    if x==13:
        break        ##stops at  13
    else:
        print(x)
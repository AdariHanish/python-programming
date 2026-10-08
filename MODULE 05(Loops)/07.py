#break contiue and pass
print("------------break-------------")
for i in range(1,11):
    if i==5:
        break
    print(i)
print("end of program")
print("------------continue-------------")
for i in range(1,11):
    if i==5:
        continue
    print(i)
print("end of program")
print("------------pass-------------")
for i in range(1,11):
    if i==5:
        pass
    print(i)
print("end of program")
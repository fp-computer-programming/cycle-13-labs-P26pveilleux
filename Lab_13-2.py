grades = {'assigment1': 85,'assigment2' : 70,'as3sigment' : 95,'assigment4' : 60,'assigment5': 45}

print(list(grades.values()))

for assignment in grades:
    print (assignment)


for assignment, grade in grades.items(): 
    if grade >= 70:
        print (f"{assignment}, {grade}")

for assignment, grade in grades.items(): 
    if grade <= 50:
        print (f"{assignment}, {grade}")



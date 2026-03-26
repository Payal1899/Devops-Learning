#Creating dictionary
Dict={}
YN='Y'
while YN!='N':
    YN=input("Do you want to add new Student and grades? Y/N\n")
    if YN=='Y':
        #Input for student name
        Name = input("Enter name of student: ")
        #Input for student grade
        grade = int(input("Enter Grades: "))
        #Adding input to dictionary
        Dict[Name]=grade
    else:
        #Input for student name
        Name = input("Enter name of student who's grades to be modified: ")
        if Name in Dict:
            #Input for student grade
            grade = int(input("Enter Grades: "))
            #Modifying student grade in dictionary
            Dict[Name]=grade
        else:
            print("Enterred student is not available")
    YN=input("Do you want to perform anymore updates? Y/N\n")

#Printing content of decitionary
print(Dict)

print( '''

###############################
# WELCOME TO MY AMUSEMENT PARK#
###############################

## Adult (over 18) : 15CAD
## Student(12-18) : 12CAD
##Children (under12) : 5CAD
##Elder (over 80) : Free/0CAD

''')
age = 19
total = 0
adult = 0
child = 0 
student = 0
elder = 0

total = {'adult': 0 , 'child' : 0, 'student' : 0, 'elder' : 0}

while age != 0:
    age = int(input("Type your age (if end of list, put 0): "))

    if age > 18 and age < 80:
        print("15CAD")
        total['adult'] += 1
        adult += 1
    elif age >= 80:
        print("0CAD")
        elder += 1
        total['elder'] += 1 
    elif age <= 18 and age > 12 :
        print("12 CAD")
        total['student'] += 1 
        student += 1
    elif age <= 12 and age > 0:
        print("5 CAD")
        child += 1
        total['child'] += 1 
    elif age == 0:
        break 

    total_pay = 15 * total['adult'] + 0 * total['elder'] + 12 * total ['student'] + 5 * total['child']

 
print(f"You need to pay total : $ {total_pay}")
print(f"number of adults : {adult}\nnumber of children : {child}\nnumber of students : {student}\nnember of elders : {elder}")

# cmb or radio to get number of adult, student, child, elder
# when button is pressed tell me how much and how much people (2 buttons) add button and done button which shows total people and how much
# combine line 47, 48 into a variable and config the label text part 
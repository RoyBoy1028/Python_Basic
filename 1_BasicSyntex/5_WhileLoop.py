score = 0   # != : not equal to
while score != 120 :  
    score = int(input("Type your math score (if you input 120, exit): "))

    if score > 90 :
        print("you got an 'A'")
    elif score <= 90 and score >80: 
        print("you got 'B'")
    elif score > 70 and score <= 80: 
        print("you got 'C'")
    else :
        print("Fail.")

import math
end=False

#OPERATOR ASSIGNING
while end==False:
    operatortrue=False
    while operatortrue==False:
        print("\nOPERATORS: 'addition' , 'subtraction' , 'division', 'multiply', 'exponent', 'square root'")
        operator=input("What is your operator?: ")
        answer=0

        #CLARIFICATION
        if operator=="-" or operator=="minus" or operator=="subtraction":
             operator="subtraction"
             operatortrue=True
        elif operator=="+" or operator=="add" or operator=="addition":
            operator="addition"
            operatortrue=True
        elif operator=="*" or operator=="times" or operator=="multiplication" or operator=="multiply":
              operator="multiply"
              operatortrue=True
        elif operator=="/" or operator=="divide" or operator=="division":
              operator="division"
              operatortrue=True
        elif operator=="**" or operator=="exponent":
              operator="exponent"
              operatortrue=True
        elif operator=="sqrt" or operator=="square root":
              operator="square root"
              operatortrue=True
        else:
            print("INVALID OPERATOR")
            continue


    #INPUT DIFFERENTIATION
    numtrue=False
    while numtrue==False:
        if operator=="division":
            
            choice1=input("Numerator: Pi or numbers?: ")
            if choice1=="pi":
                num1=math.pi
                numtrue=True
            else:
                num1=float(input("Numerator: "))
                
            choice2=input("Denominator: Pi or numbers?: ")
            if choice2=="pi":
                num2=math.pi
                numtrue=True
            else:
                num2=float(input("Denominator: "))
                numtrue=True
                
        elif operator=="addition" or operator=="multiply" or operator=="subtraction":
            
            choice1=input("Number 1: Pi or numbers?: ")
            if choice1=="pi":
                num1=math.pi
                numtrue=True
            else:
                num1=floatinput("Number 1: "))
                numtrue=True
                
            choice2=input("Number 2: Pi or numbers?: ")
            if choice2=="pi":
                num2=math.pi
                numtrue=True
            else:
                num2=float(input("Number 2: "))
                numtrue=True
                
        elif operator=="square root":        
            num2=int(input("Radicand: "))
            numtrue=True
            
        elif operator=="exponent":
            choice1=input("Number: Pi or numbers?: ")
            if choice1=="pi":
                num1=math.pi
                numtrue=True
            else:
                num1=float(input("Number 1: "))
                
            choice2=input("Exponents: Pi or numbers?: ")
            if choice2=="pi":
                num2=math.pi
                numtrue=True
            else:
                num2=float(input("Number 2: "))
                numtrue=True
            

    #CALCULATIONS
    if operator=="addition":
        answer=num1+num2
        print(f"{num1} + {num2} = {answer}")
    elif operator=="subtraction":
        answer=num1-num2
        print(f"{num1} - {num2} = {answer}")
    elif operator=="division":
        answer=num1/num2
        print(f"{num1} / {num2} = {answer}")
    elif operator=="multiply":
        answer=num1*num2
        print(f"{num1} / {num2} = {answer}")
    elif operator=="exponent":
        answer=num1**num2
        print(f"{num1} ^ {num2} = {answer}")
    elif operator=="square root":
        answer=num2**0.5
        print(f"SQRT {num2} = {answer}")

    #ROUNDING
    roundyes=input("Round?: ")

    if roundyes=="yes" or roundyes=="Yes":
        roundamount=int(input("Decimal Places?: "))
        answer=round(answer, roundamount)
        print(answer)



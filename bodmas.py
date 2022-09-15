x = input("enter the first number : ")
y = input("enter the second number: ")

if x.isnumeric and y.isnumeric():
    a=int(x)
    b=int(y)
    var = input("enter the operations : +,-,*,%,/")
    print("this is numeric")
    if var == "+":
        print("ADDITION : ",a+b)
    elif var == "-":
        print("SUBSTRACTION : ",a-b)
    elif var == "*":
        print("MULTIPLAY : ",a*b)
    elif var == "%":
        print("DIVISION : ",a%b)
    elif var == "/":
        print("REMINDER : ",a/b)
    elif x.isalpha or y.isalpha:
        print("you enter wrong input")
    
else:
    print("THIS IS AN ALPHABATE")
    
    


    
    

try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    print("which operation you want to perform:\npress + if you need to add\npress - if you need to subtract\npress*if you need multiply\npress / if you need to divide")
    o = input("Enter operation to be performed: ")
    match o:
        case "+": 
            print(f"The sum is : {a+b}")
        case "-": 
            print(f"The sum is : {a-b}")   
        case "*": 
            print(f"The sum is : {a*b}")
        case "/": 
            print(f"The sum is : {a/b}")   
except Exception as e: 
    print("Enter only integers as inputs",e)
         

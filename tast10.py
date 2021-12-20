a = int(input("please enter first namber"))
b = int(input("please enter second namber"))

op = input()

if op=="+":
    result= a+b

if op=="-":
    result= a-b

if op=="*":
    result= a*b

if op=="/":
    if b != 0 :
       result= a / b
    else:
        result= "cannot divide by zero"   
        

print(result)               
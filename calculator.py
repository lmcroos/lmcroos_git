def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
    
def main ():
    operation = input("what do you want to do (+,-,*,/): ")
    if(operation !='+' and operation !='-' and operation !='*' and operation !='/'):
        print("You must enter a valid operation")
    else:
        var1 = int(input("Enter num1: "))
        var2 = int(input("Enter num2: "))
#addition
        if(operation == '+'):
            print(add(var1, var2))
#subtraction
        elif(operation == '-'):
            print(sub(var1, var2))
#multiply
        elif(operation == '*'):
            print(mult(var1, var2))
#divide
        else:
            print(div(var1, var2))
main()       

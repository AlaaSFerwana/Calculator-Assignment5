def add(Num1,Num2):
    return Num1+Num2
def subtract(Num1,Num2):
    return Num1-Num2
def multiply(Num1,Num2):
    return Num1*Num2
def divide(Num1,Num2):
    return Num1/Num2
def operation ():
    print("Please select the operation:")
    print("A) Add")
    print("B) Subtract")
    print("C) Multiply")
    print("D) Divide")
    Select = (input("Please enter your choice from A,B,C.D : "))
    Num_1 = float(input("Enter The First Number  : "))
    Num_2 = float(input("Enter The Second Number : "))
    if Select == 'A':
        print(Num_1, "+", Num_2, "=", add(Num_1, Num_2))
    elif Select == 'B':
        print(Num_1, "-", Num_2, "=", subtract(Num_1, Num_2))
    elif Select == 'C':
        print(Num_1, "*", Num_2, "=", multiply(Num_1, Num_2))
    elif Select == 'D':
        if Num_2 == 0:
            print("Error")
        else:
            print(Num_1, "/", Num_2, "=", divide(Num_1, Num_2))
    else:
        print("This is an invalid input")
operation()

Another_Oper = input("Do you want to make another operation ?")
if Another_Oper == "yes" or Another_Oper == "Yes":
    operation()

else:
    print("Quite")


# calculater of  two numbers using class and static method 

# class
class Calculater:

#static methods
    @staticmethod
    def addition(num1,num2):
        addition = num1 + num2
        return addition
    
    @staticmethod
    def subtraction(num1,num2):
        subtraction = num1 - num2
        return subtraction
    
    @staticmethod
    def multiplication(num1,num2):
        multiplication =  num1 * num2
        return multiplication
    
    @staticmethod
    def division(num1,num2):
        division = num1 / num2
        return division

    @staticmethod
    def modual(num1,num2):
        modual = num1 % num2
        return modual

    @staticmethod
    def square(num1):
        sqr = num1 * num1 
        return sqr

    @staticmethod
    def cube(num1):
        cb = num1 * num1 * num1
        return cb 

print("------------Options-----------")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modual")
print("6. square")
print("7. cube")

input_choice = input("Enter the input (in index number) :")

if input_choice == '1' or input_choice == '2' or input_choice == '3' or input_choice == '4' or input_choice == '5':
    n1 = int(input("Enter the number 1:"))
    n2 = int(input("Enter the number 2:")) 

if input_choice == '6' or input_choice == '7':
    sqr_cube_input = int(input("Enter number for cube or square :"))

if input_choice == '1':
    sum = Calculater.addition(n1,n2)
    print(f"The addition of {n1} and {n2} is {sum}")

elif input_choice == '2':
    sub = Calculater.subtraction(n1, n2)
    print(f"The subtraction of {n1} and {n2} is {sub}")

elif input_choice == '3':
    mul = Calculater.addition(n1,n2)
    print(f"The multiplication of {n1} and {n2} is {mul}")

elif input_choice == '4':
    div = Calculater.division(n1,n2)
    print(f"The division of {n1} and {n2} is {div}")

elif input_choice == '5':
    mod = Calculater.modual(n1,n2)
    print(f"The division of {n1} and {n2} is {mod}")

elif input_choice == '6':
    sqr = Calculater.square(sqr_cube_input)
    print(f"The square of {sqr_cube_input} is {sqr}")

elif input_choice == '7':
    cb = Calculater.cube(sqr_cube_input)
    print(f"The square of {sqr_cube_input} is {cb}")

else:
    print("Input valid choice!!!!!!!")
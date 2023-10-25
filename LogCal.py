import math

def LogCalculator():
    while True:
        print("Welcome To Logarithm Calculator")
        print("Hit '1' To Calculate Custom Logarithm")
        print("Hit '2' To Calculate In '10' Base")
        print("Hit '3' To Calculate In 'ln' Base")
        choice = input("1/2/3: ")
        if choice == '1':
            num = float(input("Enter a positive number: "))
            if num > 1:
                base = float(input("Enter Custom base: "))
                if base > 0 and base != 1:
                    result = math.log(num, base)
                    print(f"Result: {result}")
                else:
                    print("Failed")
        elif choice == '2':
            num = float(input("Enter a positive number: "))
            if num > 1:
                result = math.log(num, 10)
                print(f"Result: {result}")
            else:
                print("Failed")
        elif choice == '3':
            num = float(input("Enter a positive number: "))
            if num > 1:
                result = math.log(num)
                print(f"Result: {result}")
            else:
                print("Failed")

        user_input = input("Hit Any Key To Continue Or Hit 'x' To Leave: ")
        if user_input == "x":
            break

LogCalculator()
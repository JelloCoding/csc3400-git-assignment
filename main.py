from calculator import *

def main():
    print("Welcome to the calculator!")
    print("---------------------------")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")

    choice = input("Enter your choice (1-6): ")

    # Operations that need two numbers
    if choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            try:
                print("Result:", divide(a, b))
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
        elif choice == "5":
            print("Result:", power(a, b))

    # Square root only needs one number
    elif choice == "6":
        a = float(input("Enter a number: "))
        try:
            print("Result:", square_root(a))
        except ValueError as e:
            print("Error:", e)

    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
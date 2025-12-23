def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Division by zero is not possible 🚫"
    return a / b


print("🧮 Welcome to Calculator")

option = input("Do you want to open calculator? (yes/no): ").lower()

while option == "yes":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print(" Please enter valid numbers only!")
        continue

    print("""
Choose operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Result =", addition(a, b))
    elif choice == "2":
        print("Result =", subtraction(a, b))
    elif choice == "3":
        print("Result =", multiplication(a, b))
    elif choice == "4":
        print("Result =", division(a, b))
    else:
        print("❌ Invalid choice!")

    option = input("Do you want to continue? (yes/no): ").lower()

print("✅ Thanks for using calculator. Peace ✌️")

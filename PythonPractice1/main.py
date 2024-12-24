
def data_types_demo():
    name = "Soumitra"
    age = 20
    height = 5.8
    is_student = True

    print("Name:", name)
    print("Age:", age)
    print("Height:", height)
    print("Is a student:", is_student, "\n")

def list_and_loops():
    fruits = ["Apple", "Banana", "Cherry", "Date"]
    print("Fruit List:")
    for fruit in fruits:
        print("-", fruit)
    print()

def conditional_demo():
    number = int(input("Enter a number to check if it's even or odd: "))
    if number % 2 == 0:
        print(f"{number} is even.\n")
    else:
        print(f"{number} is odd.\n")

def calculate_square(num):
    return num * num

def function_demo():
    print("Function Demo:")
    for i in range(1, 6):
        print(f"The square of {i} is {calculate_square(i)}")
    print()

def dictionary_demo():
    capitals = {"India": "New Delhi", "USA": "Washington, D.C.", "Japan": "Tokyo"}
    country = input("Enter a country to find its capital: ").strip()
    capital = capitals.get(country, "Not Found")
    print(f"The capital of {country} is {capital}.\n")

def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "undefined (cannot divide by zero)"
    else:
        result = "invalid operator"

    print("Result:", result, "\n")

def main():
    data_types_demo()
    list_and_loops()
    conditional_demo()
    function_demo()
    dictionary_demo()
    calculator()
    print("Thank you for exploring Python Basics!")

if __name__ == "__main__":
    main()

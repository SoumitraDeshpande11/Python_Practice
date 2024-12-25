def arithmetic_operations():
    print("Arithmetic Operations:")
    numbers = [5, 10, 15, 20]
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))
    print("Max:", max(numbers))
    print("Min:", min(numbers))
    print()

def file_handling_demo():
    print("File Handling Demo:")
    filename = "sample.txt"
    with open(filename, "w") as file:
        file.write("Hello, this is a sample file.\n")
        file.write("Python makes file handling easy.\n")
    print(f"Data written to {filename}")

    print("Reading from the file:")
    with open(filename, "r") as file:
        content = file.readlines()
        for line in content:
            print(line.strip())
    print()

def loop_and_conditions():
    print("Looping with Conditions:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(f"{i} is even.")
        else:
            print(f"{i} is odd.")
    print()

def introduce_class():
    print("Introducing Classes and Objects:")

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hello, my name is {self.name} and I am {self.age} years old."

    person1 = Person("Soumitra", 20)
    print(person1.greet())

    person2 = Person("Alex", 25)
    print(person2.greet())
    print()

def error_handling_demo():
    print("Error Handling Demo:")
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print(f"The result of division is {result}.")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    finally:
        print("Error handling demo completed.\n")

def main():
    arithmetic_operations()
    file_handling_demo()
    loop_and_conditions()
    introduce_class()
    error_handling_demo()
    print("Thank you for advancing with Python!")

if __name__ == "__main__":
    main()

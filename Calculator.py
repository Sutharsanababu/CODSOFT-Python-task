import math

class Calculator:
    def __init__(self):
        self.operations = {
            '1': self.add,
            '2': self.subtract,
            '3': self.multiply,
            '4': self.divide,
            '5': self.exponentiate,
            '6': self.square_root,
            '7': self.logarithm,
            '8': self.sine,
            '9': self.cosine,
            '10': self.tangent
        }

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is undefined."
        return a / b

    def exponentiate(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            return "Error: Cannot take the square root of a negative number."
        return math.sqrt(a)

    def logarithm(self, a, base=10):
        if a <= 0:
            return "Error: Logarithm of a non-positive number is undefined."
        return math.log(a, base)

    def sine(self, a):
        return math.sin(math.radians(a))

    def cosine(self, a):
        return math.cos(math.radians(a))

    def tangent(self, a):
        return math.tan(math.radians(a))

    def run(self):
        while True:
            print("\nCalculator Options:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Square Root")
            print("7. Logarithm")
            print("8. Sine")
            print("9. Cosine")
            print("10. Tangent")
            print("11. Exit")

            choice = input("Choose an operation (1-11): ")

            if choice == '11':
                print("Exiting calculator.")
                break

            if choice not in self.operations:
                print("Invalid choice. Please select a valid option.")
                continue

            try:
                if choice in ['1', '2', '3', '4', '5']:  # Two-operand operations
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    result = self.operations[choice](a, b)
                elif choice in ['6']:  # Single-operand operations
                    a = float(input("Enter the number: "))
                    result = self.operations[choice](a)
                elif choice in ['7']:  # Logarithm with optional base
                    a = float(input("Enter the number: "))
                    base = input("Enter the base (default is 10): ")
                    if base.strip() == "":
                        base = 10
                    else:
                        base = float(base)
                    result = self.logarithm(a, base)
                else:  # Trigonometric functions
                    a = float(input("Enter the angle in degrees: "))
                    result = self.operations[choice](a)

                print(f"Result: {result}")

            except ValueError:
                print("Error: Please enter a valid number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()

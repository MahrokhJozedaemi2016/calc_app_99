<<<<<<< HEAD
"""
This module serves as the entry point for the calculator application. It processes user input from the command line
and performs the requested arithmetic operation.
"""
import sys
=======
>>>>>>> origin/main
from calculator import ArithmeticEngine
from calculator.calculations import OperationHistory
from decimal import Decimal, InvalidOperation

def calculate_and_store(a, b, operation_name):
    """Performs the calculation and stores it in history."""
    # Map the operations
    operation_mappings = {
        'add': ArithmeticEngine.add,
        'subtract': ArithmeticEngine.subtract,
        'multiply': ArithmeticEngine.multiply,
        'divide': ArithmeticEngine.divide
    }
<<<<<<< HEAD

    # Unified error handling for decimal conversion
=======
    
>>>>>>> origin/main
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
<<<<<<< HEAD
        result = operation_mappings.get(operation_name)  # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)
=======
        
        # Check if the operation exists in the mapping
        operation = operation_mappings.get(operation_name)
        
        if operation:
            # Perform the operation
            result = operation(a_decimal, b_decimal)
            print(f"The result of {operation_name} between {a} and {b} is {result}")
        else:
            print(f"Unknown operation: {operation_name}")
            return
        
        # Store the operation in history
        OperationHistory.record(result)
        
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def interactive_calculator():
    print("Welcome to the interactive calculator! Type 'exit' to quit.")
    print("Type 'history' to view past calculations or 'clear_history' to clear them.")
    
    while True:
        user_input = input("Enter a command (add, subtract, multiply, divide) followed by two numbers: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'history':
            # View the history of calculations
            history = OperationHistory.retrieve_all()
            if history:
                for idx, operation in enumerate(history, 1):
                    print(f"{idx}: {operation}")
            else:
                print("No history available.")
        elif user_input.lower() == 'clear_history':
            # Clear the calculation history
            OperationHistory.clear_all()
            print("Calculation history cleared.")
        else:
            try:
                command, num1, num2 = user_input.split()
                # Perform and store the calculation
                calculate_and_store(num1, num2, command)
            except ValueError:
                print("Invalid input. Please provide a command followed by two numbers.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    interactive_calculator()
>>>>>>> origin/main


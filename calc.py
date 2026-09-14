def enter_operand(operand_number):
    operand = int(input(f"Enter your {operand_number} operand: "))
    return operand

def main():
    print("Which operation would you like to perform?")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    choice = int(input("Enter your choice: "))

    operand1 = enter_operand("first")
    operand2 = enter_operand("second")

    if choice == 1:
        result = operand1 + operand2
    elif choice == 2:
        result = operand1 - operand2
    elif choice == 3:
        result = operand1 * operand2
    elif choice == 4:
        result = operand1 / operand2
    else:
        print("Invalid choice")
        return

    print(f"Result: {result}")

main()
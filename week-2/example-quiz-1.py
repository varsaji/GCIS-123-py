# ADD TWO NUMBERS - Quiz 1 practice

def add(x, y):
# makes a function called add that takes two numbers. colon at the END.
    return x + y
# hands the total back. indented because it's inside the function.

def main():
# makes the main function. colon at the end again.
    a = int(input("Enter the first number: "))
# ask for the first number. int() turns the text into a real number.
    b = int(input("Enter the second number: "))
# ask for the second number, also turned into a number.
    answer = add(a, b)
# call the add function and save what it returns into answer.
    print("The answer is", answer)
# print the result on screen.

main()
# runs the program. NOT indented -> it's outside the function.

# 3 things that make it correct:
#   1) def name():   -> colon at the END
#   2) indent everything INSIDE a function
#   3) int(input(...)) -> so 4 + 6 = 10, not "46"
import traceback

import addition as add
import subtraction as sub
import multiplication as mul
import division as div

print("Welcome to a simple [probably terrible] calculator User!")

print("Please select a mathimatical method from the following options: ")
method_statement = ["1: Addition", "2: Subtraction", "3: Multiplication", "4: Division"]
for statement in method_statement:
    print(statement)

try: 
    method = int(input("Please enter your method: "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ZeroDivisionError:
    print("Bruh, you can't divide by 0, don't even try") 
except ValueError:
    print("dude, you can't just put a word and expect this terrible app to work")
except:
    traceback.print_exc()
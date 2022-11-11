from logging import raiseExceptions
import re


class Calculator:

    def __init__(self) -> None:
        pass

    def sub(self, num1, num2):
        return num1 - num2

    def add(self, num1, num2):
        return num1 + num2

    def mult(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2


add_regex = re.compile(r'(\d+) \+ (\d+)')
sub_regex = re.compile(r'(\d+) - (\d+)')
mul_regex = re.compile(r'(\d+) \* (\d+)')
div_regex = re.compile(r'(\d+) / (\d+)')


exit_command = 'Exit'
calculator = Calculator()
command = input("Enter Your Phrase : ")

while command != exit_command:
    
    if add_regex.match(command):
        num1, num2 = add_regex.search(command).groups()
        res = calculator.add(int(num1), int(num2))
        print(f'Result : {res}')
    elif sub_regex.match(command):
        num1, num2 = sub_regex.search(command).groups()
        res = calculator.sub(int(num1), int(num2))
        print(f'Result : {res}')
    elif mul_regex.match(command):
        num1, num2 = mul_regex.search(command).groups()
        res = calculator.mult(int(num1), int(num2))
        print(f'Result : {res}')

    elif div_regex.match(command):
        num1, num2 = div_regex.search(command).groups()
        res = calculator.div(int(num1), int(num2))
        print(f'Result : {res}')
    else:
        print('Invalid Command')

    command = input("Enter Your Phrase : ")






print("Clculator process is done!")
print("If you have other orders, restart the calculator.")
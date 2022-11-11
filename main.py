from logging import raiseExceptions
import re


class Calculator:

    def __init__(self) -> None:
        pass

    def sub(self, num1, num2):
        sub = num1 - num2
        return sub

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


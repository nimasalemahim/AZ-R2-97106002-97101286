from logging import raiseExceptions
import re


class Calculator:

    def __init__(self) -> None:
        pass

    def sub(self, num1, num2):
        try:
            sub = num1 - num2
            return sub
        except:
            raiseExceptions("subtraction is not valid!")
        
add_regex = re.compile(r'(\d+) \+ (\d+)')
sub_regex = re.compile(r'(\d+) - (\d+)')
mul_regex = re.compile(r'(\d+) \* (\d+)')
div_regex = re.compile(r'(\d+) \% (\d+)')


exit_command = 'Exit'
calculator = Calculator()
command = input("Enter Your Phrase : ")

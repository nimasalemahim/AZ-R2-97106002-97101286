import re


class Calculator:

    def __init__(self) -> None:
        pass


add_regex = re.compile(r'(\d+) \+ (\d+)')
sub_regex = re.compile(r'(\d+) - (\d+)')


exit_command = 'Exit'
calculator = Calculator()
command = input("Enter Your Phrase : ")

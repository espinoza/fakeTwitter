import re

def contains_digit(string):
    """Returns True if the string contains at least one digit."""
    digit_regex = re.compile('\d')
    return digit_regex.search(string)

def contains_uppercase(string):
    """Returns True if the string contains at least one uppercase letter."""
    upper_regex = re.compile('[A-Z]')
    return upper_regex.search(string)

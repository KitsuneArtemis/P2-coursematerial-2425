# Write your code here
import re

def one_or_more_abc(string):
    regex = r'^(abc)+$'
    return re.match(regex, string)
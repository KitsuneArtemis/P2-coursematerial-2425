# Write your code here
import re

def two_or_more_abc(string):
    regex = r'^abc(abc)+$'
    return re.match(regex, string)
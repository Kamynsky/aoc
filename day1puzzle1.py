#!~/usr/bin/python3
import re
sum=0
pattern_two_digits=r'\D*(\d).*?(\d)\D*$'
pattern_one_digit=r'\D*(\d).*'
with open('input.txt','r') as file:
    for line in file:
        match = re.search(pattern_two_digits, line)
        if match:
            found_digits=match.group(1) + match.group(2)
            print(found_digits)
            sum=int(found_digits)+sum
            print(sum)
        else:
            match = re.search(pattern_one_digit, line)
            found_digits=match.group(1) + match.group(1)
            sum=int(found_digits)+sum
            print(sum)
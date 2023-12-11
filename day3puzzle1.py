# find numbers that are next to special char on the same line and +1 -1 index on the line over or below it
# use index of numbers and special chars and comepere them to find adjecant ones , use try as a method to trying ?
# we need to read 3 lines so we can compare middle to upper and below , this will ofc not work with first and last line 
#or mayben we can go line by line and just look form indexes and compare them to next line?
import re
input_file='day3puzzle.txt'
speccharpattern=r'[^a-zA-Z0-9]'
with open(input_file,'r') as file:
    for line in file:
        special_chars=line.replace('.','').rstrip()
        special_chars=re.findall(speccharpattern,special_chars)
        print(special_chars)
#         for i, char in enumerate(line):
#             if char.isdigit():
#                 index_iterate = i
#                 print(index_iterate)
#             elif char==
        
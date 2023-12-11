# find numbers that are next to special char on the same line and +1 -1 index on the line over or below it
import re
input_file='day3puzzle.txt'
speccharpattern=r'[^a-zA-Z0-9]'

print(speccharpattern)
with open(input_file,'r') as file: #open file containing strings 
    for line in file: # go line by line
        numberremover=str.maketrans('','','0123456789')
        nodigi=line.translate(numberremover)
        nodot=nodigi.replace('.','')
        #print(nodot)
        specchar=re.findall(speccharpattern,line)
        print(specchar)
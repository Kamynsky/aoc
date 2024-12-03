# search for mul(xxx,yyy) in input /// using regex , probably good idea to group numbers and multi them on spot and start adding . Can be solved in couple of lines
# multiplay xxx and yyy
# sum multiplication
import re
with open('day3input.txt','r') as f:
    input = " ".join(line.rstrip() for line in f)
    mullist=re.findall("mul\([0-9]+,[0-9]+\)",input)
    for item in mullist:
        
    

# search for mul(xxx,yyy) in input /// using regex , probably good idea to group numbers and multi them on spot and start adding . Can be solved in couple of lines
# multiplay xxx and yyy
# sum multiplication
import re
sollution=0
with open('day3input.txt','r') as f:
    input = " ".join(line.rstrip() for line in f)
    lookingfor=re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    for match in lookingfor.finditer(input):
        x=int(match.group(1))
        y=int(match.group(2))
        multiplication=x*y
        sollution+=multiplication
        print(sollution)
 

        
    

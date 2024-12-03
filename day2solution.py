# One line , one report = line.split()
# Max diff between consequitve numbers <-/+3 , only increasing or decreasing vecotr
# Solltuion is amount of safe reports
i=0
with open("day2input.txt","r") as input:
    for line in input:
        line=line.split()
        lsize=(len(line))
        for i in range(lsize):
            i-=1
            diff=int(line[i])-int(line[i+1])
            i+=3
        for i in range(len(line)):
            diff=line[i]
            print(diff)
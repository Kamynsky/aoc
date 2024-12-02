# One line , one report = line.split()
# Max diff between consequitve numbers <-/+3 , only increasing or decreasing vecotr
# Solltuion is amount of safe reports
with open("day2input.txt","r") as input:
    for line in input:
        line=line.split()
        lsize=(len(line))
        for i in range(lsize):
            n=0
            while n<lsize:
                diff=int(line[i]) - int(line[i+1])
                n+=1
                print(diff)
            #diff=int(line[i])-int(line[i+1])
        # for i in range(len(line)):
        #     diff=line[i]
        #     print(diff)
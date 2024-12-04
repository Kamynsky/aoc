# One line , one report = line.split()
# Max diff between consequitve numbers <-/+3 , only increasing or decreasing vecotr
# Solltuion is amount of safe reports
# numpy would be easier but lets do everything manually
count=0
with open("day2input.txt","r") as input:
    for line in input:
        line=line.split()
        lsize=(len(line))
        print(line)
        i=1
        while i in range(lsize):
            diff=int(line[i-1]) - int(line[i])
            print(diff)
            i+=1
            while diff in range(-3,3):
                print("diff ok")
                continue
            else:
                print("diff bad")
            
            





            
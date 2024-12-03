# sort left and right pad by smallest to the highest
# get numebers diference from left to right , number is always positive and int
# add all distances
input=open("day1input.txt","r")
leftpad=[]
rightpad=[]
diff=[]
for line in input:
    addcoma=line.split()
    leftpad.append(int(addcoma[0]))
    rightpad.append(int(addcoma[1]))
leftpad.sort()
rightpad.sort()
for i in range(len(rightpad)):
    distance=(leftpad[i]-rightpad[i])
    if distance <0:
        distance=distance*-1
        diff.append(distance)
    else:
        diff.append(distance)
# print("leftpad",leftpad)
# print("rightpad",rightpad)
# print("diff",diff)
print("Distance Sum",sum(diff))

import pdb
index_list=[]
n=0
with open('gsaoc.txt','r') as file:
    for line in file:
        for i, char in enumerate(line):
            if char=='L':
                try:
                    index_list[n-1]
                except IndexError as e:
                    index_list.append(i)
                else:
                    if index_list[n-1] - i in {1,0,-1}:
                        index_list.append(i)
                        n+=1
                        print(index_list)
                    
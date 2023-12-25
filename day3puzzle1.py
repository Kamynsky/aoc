# find numbers that are next to special char on the same line and +1 -1 index on the line over or below it
# use index of numbers and special chars and comepere them to find adjecant ones , use try as a method to trying ?
# we need to read 3 lines so we can compare middle to upper and below , this will ofc not work with first and last line 
#or mayben we can go line by line and just look form indexes and compare them to next line?

#--------------------------------------------------------------------------------------------------------------------------
#File download, day var set 
#--------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/env python3
import urllib.request
import os
file_with_path = os.path.abspath(__file__)
file_name = os.path.basename(file_with_path)
day=file_name[3]
input_file='day'+day+'input.txt'
def input_file_request():
    if os.path.exists(input_file):
        print('File already exists, no need to download it again')
    else:
        coockie_file='acoecoockie.txt'
        with open(coockie_file,'r') as file:
            coockie=file.read().strip()
            url="http://adventofcode.com/2023/day/"+day+"/input"
            request = urllib.request.Request(url)
            request.add_header('Cookie', coockie)
            response = urllib.request.urlopen(request)
            with open(input_file,'wb') as fileinput:
                fileinput.write(response.read())
response = input_file_request()

#--------------------------------------------------------------------------------------------------------------------------
#Code for puzzle
#--------------------------------------------------------------------------------------------------------------------------
grid=[]
digit_list=[]
characters_list=[]
with open(input_file,'r') as file:      # import file content as grid
    for line in file:
        grid.append(line.strip())

row_size=len(grid) # grid row lenght
column_size=len(grid[0]) # grid column lenght

for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item.isdigit():
            digit_list.append([item,i,j])
        elif item !='.':
            characters_list.append([item,i,j])

for digit,column,row in digit_list:
    

            
            
            
# def symbol_checker(char):
#     return (not char.isdigit()) and char != '.'

# def digit_index_checker(index):    

# def symbol_presence_checker(index_start,index_end):

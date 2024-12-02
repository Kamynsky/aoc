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
grid = []
digit_list = []
characters_list = []
numbers_list = ()

with open(input_file, 'r') as file:  # import file content as grid
    for line in file:
        grid.append(line.strip())

row_size = len(grid)  # grid row length
column_size = len(grid[0])  # grid column length

for i, row in enumerate(grid):
    for j,column in enumerate(row):
        for digit in column:
            if digit.isdigit():
                digit_list.append((digit,i,j))

numbers_list = []
current_number = None
start_index = None

for digit, row, column in digit_list:
    current_number += str(digit)  # Concatenate the digit as a string

    if start_index is None:
        start_index = column

    for i in range(len(digit_list) - 1):
        digit, row, column = digit_list[i]
        next_digit, next_row, next_column = digit_list[i + 1]

        current_number += str(next_digit)  # Concatenate the next digit as a string

        if next_column != column + 1 or next_digit != digit + 1:
            end_index = column
            numbers_list.append([int(current_number), row, start_index, end_index])
            current_number = ""
            start_index = None

# Handle the last digit separately
digit, row, column = digit_list[-1]
current_number += str(digit)
end_index = column
numbers_list.append([int(current_number), row, start_index, end_index])

# Print the result
for result_tuple in numbers_list:
    print(result_tuple)
    
    
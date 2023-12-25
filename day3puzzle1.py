# find numbers that are next to special char on the same line and +1 -1 index on the line over or below it
# use index of numbers and special chars and comepere them to find adjecant ones , use try as a method to trying ?
# we need to read 3 lines so we can compare middle to upper and below , this will ofc not work with first and last line 
#or mayben we can go line by line and just look form indexes and compare them to next line?
import urllib.request
day=str(3)
def input_file_request():
    coockie_file='c:/acoecoockie.txt'
    with open(coockie_file,'r') as file:
        coockie=file.read().strip()
        url="http://adventofcode.com/2023/day/"+day+"/input"
        request = urllib.request.Request(url)
        request.add_header('Cookie', coockie)
        response = urllib.request.urlopen(request)
        return response
response = input_file_request()
input=response.read().decode('utf-8')
print(input)
            

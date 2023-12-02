#!~/usr/bin/python3
import urllib.request

url='https://adventofcode.com/2023/day/1/input'
requestfile=urllib.request.urlopen(url)
for line in requestfile:
    print(line)

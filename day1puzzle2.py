# Puzzle 1 is to find first and last digit in the input file , if there is only one digit it is used twice as first and last digit
# Puzzle 2 is to find and replaced english words for number with digits and use previous code to provide sum . Meaning two in string becomes 2 etc.
import re #Import Regex Lib to search for Digits
sum=0 # Initialize Sum which is needed for answer 
pattern_two_digits=r'\D*(\d).*?(\d)\D*$' # Regex Pattern for Two digit search
pattern_one_digit=r'\D*(\d).*' # Regex pattern for single digit search
input_file='day1puzzle1.txt'
word_to_digit={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9} # dictionary used for searching and replacing word to digit
with open(input_file,'r') as file: #open file containing strings 
    for line in file: # go line by line
        match = re.search(pattern_two_digits, line) # search for first and last digit
        if match: 
            found_digits=match.group(1) + match.group(2) # If two digits are found combine them in to two digit number . 7 and 7 becomes 77
            sum=int(found_digits)+sum # add to sum var for answer 
        else: # if two digits are not found 
            match = re.search(pattern_one_digit, line) # look for singe digit in the string
            found_digits=match.group(1) + match.group(1) # combine one digit found in to 2 digit number . Meaning 5 becomes 55
            sum=int(found_digits)+sum # add to the sum which is answer for to the puzzle
    print(sum) # print answer
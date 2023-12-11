# Find highest number per cube color per game 
# multiple rgb highest numbers by themselfs and add from all games 
import re
sum=0
pattern_cube_red_and_value=r"(\d+)red"
pattern_cube_green_and_value=r'(\d+)green'
pattern_cube_blue_and_value=r'(\d+)blue'
game_id_pattern=r'Game.(\d+):'
with open('day2puzzle.txt','r') as input:
    for line in input:
        id=re.search(game_id_pattern,line) # search for id 
        line_without_id=re.sub(game_id_pattern,'',line) # remove GAME xx:
        line_without_id=line_without_id.strip('\n').replace(' ','').replace(';',',') # remove new line white char , remove spaces , replace ; with ,
        red=re.findall(pattern_cube_red_and_value,line_without_id) #find red values
        red=[int(red_str) for red_str in red] # convert red values from str to int
        max_red=max(red) # find max value for red
        green=re.findall(pattern_cube_green_and_value,line_without_id)
        green=[int(green_str) for green_str in green]
        max_green=max(green)
        blue=re.findall(pattern_cube_blue_and_value,line_without_id)
        blue=[int(blue_str) for blue_str in blue]
        max_blue=max(blue)
        multiply=max_red*max_green*max_blue # multiply found max values
        sum+=multiply # sum multipications
    print(sum)


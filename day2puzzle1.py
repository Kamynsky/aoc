# We are determinating which games are possible and then suming up Game ID 
# 12 red cubes , 13 green cubes , 14 blue cubes are the max value
# Colors are not sorted, number of cubes are always first , name of the color latter example 4 red, 10 blue , 12 green

import re
sum=0
red_max_value=12
green_max_value=13
blue_max_value=14
pattern_game_id=r"(\d+):"
pattern_cube_red_and_value=r".(\d+).red."
pattern_cube_green_and_value=r'.(\d+).green.'
pattern_cube_blue_and_value=r'.(\d+).blue.'
with open('day2puzzle.txt','r') as input:
    for line in input:
        state=False
        
        red=re.findall(pattern_cube_red_and_value,line)
        for value in red:
            int_value=int(value)
            if int_value > red_max_value:
                state=True  
                break
        if state:
            continue
            
        green=re.findall(pattern_cube_green_and_value,line)
        for value in green:
            int_value=int(value)
            if int_value > green_max_value:
                state=True  
                break
        if state:
            continue
        
        blue=re.findall(pattern_cube_blue_and_value,line)
        for value in blue:
            int_value=int(value)
            if int_value > blue_max_value:
                state=True  
                break
        if state:
            continue
        
        if not state:
            gameid=re.search(pattern_game_id,line)
            print("Game ID to sum:",gameid.group(1))
            sum=sum + int(gameid.group(1))
            print("Current Sum :",sum)
            print(line)
import re
sum=0
id=0
red_max_value=12
green_max_value=13
blue_max_value=14
game_id_pattern=r'Game.(\d+):'
pattern_cube_red_and_value=r"(\d+)red"
pattern_cube_green_and_value=r'(\d+)green'
pattern_cube_blue_and_value=r'(\d+)blue'


with open('day2puzzle.txt','r') as input:
    for line in input:
        state=False
        id=re.search(game_id_pattern,line)
        id=id.group(1)
        line_without_id=re.sub(game_id_pattern,'',line)
        line_without_id=line_without_id.strip('\n').replace(' ','')
        game_record=re.split(r'[;]',line_without_id)
        redsum=0
        for element in game_record:
            red=re.findall(pattern_cube_red_and_value,element)
            red_value=0
            for value in red:
                red_value+=int(value)
                if red_value > red_max_value:
                    state=True  
                    break
            if state:
                break
        if state:
            continue
        else:
            green=re.findall(pattern_cube_green_and_value,element)
            green_value=0
            for value in green:
                if green_value > green_max_value:
                    state=True  
                    break
            if state:
                break
        if state:
            continue
        else:
            blue=re.findall(pattern_cube_blue_and_value,element)
            blue_value=0
            for value in blue:
                if blue_value > blue_max_value:
                    state=True  
                    break
            if state:    
                break
        if state:
            continue
        else:
            print(id)
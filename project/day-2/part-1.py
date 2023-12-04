import numpy as np
import re

with open('project/.puzzles/puzzle-2.txt') as f:
    # Read file
    contents = f.read()

    # Convert string into array (per line)
    contents = contents.split('\n')

    # ------------------------- # Get every line # ------------------------- #
    new_content = []  # Take only index "1 until end"
    for content in contents:
        new_content.append(content.split('; '))

    # ------------------------- # Split between "Game" & Value # ------------------------- #
    new_content_again = []  # Take only index 0
    for content in new_content:
        new_content_again.append(content[0].split(': '))

    # ------------------------- # Split between "Game" & Value (Part 2) # ------------------------- #
    values = []
    game = []
    counter = 0

    for content in new_content_again:
        values.append([[content[1]], new_content[counter][1:]])
        game.append(content[0])
        counter += 1

    # ------------------------- # Turn 2D list into 1D list # ------------------------- #
    new_values = []
    for value in values:
        new_values.append([j for sub in value for j in sub])

    # ------------------------- # Function for checking # ------------------------- #
    def red(value):
        regexed = ''.join(re.findall(r'\d+', value))
        if int(regexed) > 12:
            return False
        return True

    def green(value):
        regexed = ''.join(re.findall(r'\d+', value))
        if int(regexed) > 13:
            return False
        return True

    def blue(value):
        regexed = ''.join(re.findall(r'\d+', value))
        if int(regexed) > 14:
            return False
        return True

    # ------------------------- # Checking 1 # ------------------------- #
    new_values_again = []
    for value in new_values:
        temp_list = []
        for subvalue in value:
            subvalue = subvalue.split(", ")
            for sub2value in subvalue:
                if 'red' in sub2value:  # red cube
                    temp_list.append(red(sub2value))
                elif 'green' in sub2value:  # Green cube
                    temp_list.append(green(sub2value))
                elif 'blue' in sub2value:  # Blue cube
                    temp_list.append(blue(sub2value))

        new_values_again.append(temp_list)

    # ------------------------- # Checking 2 # ------------------------- #
    game_counter = 0

    possible_game = []
    for value in new_values_again:
        new_game = ''.join(re.findall(r'\d+', game[game_counter]))
        game_counter += 1
        # print(value)

        if False in value:
            continue
        else:
            possible_game.append(int(new_game))

    # ------------------------- # RESULT # ------------------------- #
    # List of possible game
    print(possible_game)

    # Sum of all possible game
    print(np.sum(possible_game))

# Import
import numpy as np
import re


# Numbers dict
numbers = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}


# Read file
with open('project/.puzzles/puzzle-1.txt') as f:
    # Read file
    contents = f.read()

    # Convert string into list
    contents = contents.split()

    # ===== # Process 1 # ===== #
    new_contents = []

    # Indexing every element on list
    for content in contents:
        # A temporary list whose contents will be added to the "new_content" list
        temp_contents = []

        for key in numbers.keys():  # Get every keys from dictionary
            if key in content:
                reg_content = re.findall(key, content)  # Filtering

                if len(reg_content) > 1:
                    temp_contents.append(''.join(reg_content[0]))
                elif len(reg_content) == 1:
                    temp_contents.append(''.join(reg_content))

        # Add "new_contents" list with "temps_contents" elements
        new_contents.append(temp_contents)

    # ===== # Process 2 # ===== #
    list_content = []
    list_count = 0

    for content in contents:
        get_list = new_contents[list_count]
        list_count += 1

        if len(get_list) > 1:
            i_dict = {}

            for i in get_list:
                i_dict.update({content.find(i): i})
            list_content.append(
                int(numbers[i_dict[min(i_dict)]] + numbers[i_dict[max(i_dict)]]))

        elif len(get_list) == 1:
            list_content.append(
                int(numbers[get_list[0]] + numbers[get_list[0]]))

    print(list_content)

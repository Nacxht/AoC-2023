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
numbers_key = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
real_num = [str(i) for i in range(1, 10)]

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

    # Testing
    # contents = ['twofive2fourfive1dvnrrvjr']

    # Checking
    def checkDupe(check, string):
        regex = re.findall(check, string)
        # print(regex)

        if len(regex) > 1:
            return True

    for content in contents:
        # get_list = new_contents[9]
        # print(get_list)
        get_list = new_contents[list_count]
        list_count += 1

        # Jika diawali dan diakhiri dengan angka
        if content[0] in real_num and content[-1] in real_num:
            list_content.append(
                int(content[0] + int(content[-1]))
            )

        # Jika kalimat diawali atau diakhiri tanpa angka
        elif content[0] in real_num and content[-1] not in real_num:
            content_num = re.findall(r'\d+', content)
            i_dict = {}
            i_arr = []

            for i in get_list:
                if checkDupe(i, content):
                    indexes = re.findall(i, content)
                    i_dict.update({content.rfind(''.join(indexes[-1:])): i})

                else:
                    i_dict.update({content.find(i): i})

            print(content_num[-1])

            list_content.append(
                int(content[0] + numbers[i_dict[max(i_dict)]]))

        elif content[-1] in real_num:
            pass

        elif len(get_list) > 1:
            i_dict = {}

            for i in get_list:
                if checkDupe(i, content):
                    indexes = re.findall(i, content)
                    i_dict.update({content.find(''.join(indexes[:1])): i})
                    i_dict.update({content.rfind(''.join(indexes[-1:])): i})

                else:
                    i_dict.update({content.find(i): i})

            list_content.append(
                int(numbers[i_dict[min(i_dict)]] + numbers[i_dict[max(i_dict)]]))

        elif len(get_list) == 1:
            list_content.append(
                int(numbers[get_list[0]] + numbers[get_list[0]]))

    # print(list_content)
    print(list_content)

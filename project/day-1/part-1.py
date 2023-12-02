# Import
import re
import numpy as np


with open('project/.puzzles/puzzle-1.txt') as f:
    # Read file
    contents = f.read()

    # Convert string into array
    contents = contents.split()

    # Get the number
    new_contents = []

    for content in contents:
        # Using regexp
        content_num = re.findall(r'\d+', content)
        content_num = ''.join(content_num)
        new_contents.append(content_num)

        # Store the summary
        sum = []

    # Get the first number and last number
    for content in new_contents:
        if len(content) == 1:
            sum.append(int(content + content))
            pass
        else:
            sum.append(int(content[:1] + content[-1:]))

    # Output
    print(np.sum(sum))

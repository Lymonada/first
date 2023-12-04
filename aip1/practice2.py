import sys
import re

file_name = sys.argv[1]

count = 0
with open(file_name) as file:
    lines = [x.strip() for x in file.readlines()]
    for word in lines:
        count += 1
        if not re.fullmatch(r'.*[0-9]+.*', word):
            print(count)
            break
            
    


        
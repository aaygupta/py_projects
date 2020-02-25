#### Code for Flixbus Interview Test

import re

# S = '00-44  48 5555 8361'
# S = '0 - 22 1985--324'
S = '555372654'

# def solution(S):
my_string = re.sub(r'-|\s','',str(S))

if len(my_string) % 2 == 0:
    str1 = '-'.join(my_string[i:i+3] for i in range(0,len(my_string),3))
    if re.search(r'-\d$',str1) != None:
        str_slice = str1[-5:].replace('-','')
        # final_str = str1[:-5] + '-'.join(str_slice[i:i+2] for i in range(0,len(str_slice),2))
        final_str = str1[:-5] + str_slice[:2] + '-' + str_slice[2:]
        # return final_str
        print(final_str)
    else:
        # return str1
        print(str1)

else:
    str1 = re.findall(r'\d{3}',my_string)
    final_str = '-'.join(str1)
    # return final_str
    print(final_str)
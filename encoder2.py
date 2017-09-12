#!/usr/bin/env python3

import string
import math

base64 = [chr(i) for i in range(49, 115)]
max_safe_int = (1 << 53) - 1


def int2base(a, b):
    return ''.join(
            [(string.digits + string.lowercase + string.uppercase)[(a/b**i) % b]
                for i in range(int(math.log(a, b)), -1, -1)]
            )


fb = """
          ###         ###
        #######     #######
      ###     ###############
    ####        ###   ##    ####
  ####           #            ###
 ###                          ##
  ##                           ##
   ##                           ##
    ##       \     \     \       ##
     ##       \     \     \    ###
      ##       \     \    ### ###
       ###      \     ##########
        ### ##########   ####
         #####          ###
            ###      ###
               ######
                 ##
"""


j = 0
c = None
positions = {}

for i, char in enumerate(fb.replace('\n', '')):
    if char != ' ':
        if char not in positions:
            positions[char] = [i]
        else:
            positions[char] += [i]

encoded = []

for char, indexes in positions.items():
    print(char, indexes)
    n = ['']
    for i in indexes:
        s = str(i)
        nn = n[-1] + s
        if int(nn) > max_safe_int:
            n += [s]
        else:
            n[-1] += s
    print(n)
    n = [int2base(int(i), 36) for i in n]
    print(n)
    encoded.append([char, n])

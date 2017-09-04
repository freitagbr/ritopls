#!/usr/bin/env python3
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

lines = fb.split("\n")
encodes = [" ", "#", "\\"]
chars = []
encoded = []

for line in lines:
    chars.append([])
    char = chars[-1]
    for c in line:
        if len(char) == 0:
            char.append(c)
        elif c == char[-1][0]:
            char[-1] = char[-1] + c
        else:
            char.append(c)

for line in chars:
    e = []
    encoded.append(e)
    i = 0
    for group in line:
        while group[0] != encodes[i]:
            e.append('a')
            i = (i + 1) % 3
        e.append(chr(len(group) + 97))
        i = (i + 1) % 3

encoded = [''.join(s) for s in encoded]

print(encoded)

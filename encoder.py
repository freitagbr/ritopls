#!/usr/bin/env python3

base64 = [chr(i) for i in range(49, 115)]

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



lines = fb.split("\n")
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
    for group in line:
        c = group[0]
        l = len(group)
        l = l + 32 if c == '#' else l
        if c == '\\':
            e.append('/')
        else:
            e.append(base64[l-1])

encoded = [''.join(s) for s in encoded]

new_fist = ''
for code in encoded:
    for char in code:
        if char == "/":
            new_fist += "\\"
        else:
            i = base64.index(char) + 1
            if i < 32:
                new_fist += " " * (i)
            else:
                new_fist += "#" * (i - 32)
    new_fist += "\n"

# for code in encoded:
#     for i, char in enumerate(code):
#         val = ord(char) - 97
#         if i % 3 == 0:
#             new_fist += " " * val
#         elif i % 3 == 1:
#             new_fist += "#" * val
#         elif i % 3 == 2:
#             new_fist += "\\" * val
#     new_fist += "\n"

print('0'.join(encoded[1:-1]))
print(new_fist)

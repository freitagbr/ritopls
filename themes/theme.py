#!/usr/bin/env python3

import json
import sys
import os

dir = os.path.dirname(os.path.realpath(__file__))
template_file = os.path.join(dir, 'base16theme.template')
json_file = sys.argv[1]

with open(json_file) as f:
    bases = json.loads(f.read())

with open(template_file) as f:
    template = f.read()

for base, color in bases.items():
    template = template.replace(base, color)

theme_file = json_file.replace('json', 'theme')

with open(theme_file, 'w') as f:
    f.write(template)

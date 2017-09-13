#!/usr/bin/env python3

import json
import sys
import os


def write_template(template_file, bases):
    with open(template_file) as f:
        template = f.read()
    for base, color in bases.items():
        template = template.replace(base, color.upper())
    return template


def write_theme(template, json_file, name):
    theme_name = os.path.splitext(json_file)[0]
    theme_file = '{}_{}.theme'.format(theme_name, name)
    with open(theme_file, 'w') as f:
        f.write(template)


if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    json_file = sys.argv[1]
    template_files = ((os.path.join(dir, '{}.template'.format(name)), name)
                      for name in ['light', 'dark'])

    with open(json_file) as f:
        bases = json.loads(f.read())

    templates = ((write_template(template, bases), name)
                 for template, name in template_files)

    for template, name in templates:
        write_theme(template, json_file, name)

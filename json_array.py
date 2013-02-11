#!/usr/bin/env python3
# coding: utf-8
# json_tables.py: convert json to html tables by making assumptions

from functools import reduce
from json import load
from sys import argv, exit, stderr


def _printrow(item, bgcolor="#FFFFFF"):
    """
    Prints *item* as HTML table rows.

    The row background color can be set with *bgcolor*.  If not set it
    defaults to "#FFFFFF".
    """
    print('  <tr bgcolor="%s">' % (bgcolor))
    [print("    <td>%s</td>" % (str(i))) for i in item]
    print('  </tr>')


def render(list_obj):
    """
    Renders a list *list_obj* as an HTML table.
    """
    print('<table border="1">')
    str_and = lambda x, y: x and isinstance(y, str)
    contains_header = reduce(str_and, list_obj[0], True)
    if contains_header:
        _printrow(list_obj[0], bgcolor="#B2D1B2")
        list_obj = list_obj[1:]
    for item in list_obj:
        _printrow(item, bgcolor="#E8EBC0")
    print('</table>')


def walk(obj):
    """
    Walk the json recursively and sniff out JSON arrays.
    """
    if isinstance(obj, dict):
        for v in obj.values():
            walk(v)
    elif isinstance(obj, list):
        render(obj)


if __name__ == "__main__":
    # process all inputs as json files
    if len(argv) <= 1:
        print('usage: json_to_tables <file>', file=stderr)
        exit(1)

    for arg in argv[1:]:
        with open(arg, 'r') as jsonf:
            json = load(jsonf)
            walk(json)

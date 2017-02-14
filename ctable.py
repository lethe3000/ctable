#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Print colorful(256) tables for terminal
    with built-in themes: dark, blue, red, green
Based on tabulate 0.7.7
"""
from collections import namedtuple
from tabulate import tabulate

Color = namedtuple("Color", ["fg", "bg"])
ColorStyle = namedtuple("ColorStyle", ["head", "row"])

_color_templates = {'dark':
                    ColorStyle(head=Color(fg=15, bg=0),
                               row=[Color(fg=15, bg=0)]
                               ),
                    'blue':
                    ColorStyle(head=Color(fg=3, bg=18),
                               row=[Color(fg=15, bg=18)]
                               ),
                    'red':
                    ColorStyle(head=Color(fg=15, bg=196),
                               row=[Color(fg=236, bg=15),
                                    Color(fg=236, bg=254)
                                    ]
                               ),
                    'green':
                    ColorStyle(head=Color(fg=15, bg=41),
                               row=[Color(fg=236, bg=15),
                                    Color(fg=236, bg=254)
                                    ]
                               ),
}


def coloration(color, text):
    if color:
        bits = list()
        bits.append('\033[38;5;%dm' % color.fg)
        bits.append('\033[48;5;%dm' % color.bg)
        bits.append(text)
        bits.append('\033[0m')
        return ''.join(bits)
    return text


def table(tabular_data, headers=(), tablefmt='plain', colorfmt='dark'):
    before_colorize = tabulate(tabular_data, headers, tablefmt=tablefmt).split('\n')
    if tablefmt == 'plain':
        if not isinstance(colorfmt, ColorStyle):
            colorfmt = _color_templates.get(colorfmt, _color_templates['dark'])
        data_index = 0
        if headers:
            before_colorize[0] = coloration(colorfmt.head, before_colorize[0])
            data_index = 1

        alter_count = len(colorfmt.row)
        for i in range(data_index, len(before_colorize)):
            before_colorize[i] = coloration(colorfmt.row[(i - data_index) % alter_count], before_colorize[i])
    return '\n'.join(before_colorize)


if __name__ == '__main__':
    row = [["Alice","F",24],["Bob","M",19],["Carlos","M",19]]
    header = ['name', 'male', 'age']

    for colorfmt in ['dark', 'green', 'red', 'blue']:
        print table(row, header, colorfmt=colorfmt)
        print

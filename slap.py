# -*- coding: UTF-8 -*-

from random import choice

import hexchat

__module_name__ = 'Slapper'
__module_version__ = '0.1'
__module_description__ = 'A Slap plugin for HexChat'
__module_author__ = 'ComputerTech'
 
slaps = [
    'slaps {} around a bit with a large trout',
    'slaps {} around a bit with a extra large dildo',
    'slaps {} around a bit with a large wet towel',
    'slaps {} around a bit with a large beer',
    'slaps {} around a bit with a small pussy',
]

def slap(word, word_eol, userdata):
    if len(word) > 1:
        hexchat.command('me ' + choice(slaps).format(word[1]))
    else:
        hexchat.command('help slap')
    return hexchat.EAT_ALL
 
hexchat.hook_command('slap', slap, help="Syntax: /slap <nick>")
hexchat.prnt(__module_name__ + " loaded.")

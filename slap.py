__module_name__ = 'Slapper'
__module_version__ = '0.0.1'
__module_description__ = 'Slapper'
__author__ = 'ComputerTech'

import hexchat

def slapper(word, word_eol, userdata):


        hexchat.command("me slaps \002{}\002 around a bit with a large trout.".format(word[1]))

        return hexchat.EAT_ALL


hexchat.hook_command('slap',slapper,)


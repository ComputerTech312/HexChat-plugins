# -*- coding: UTF-8 -*-

import hexchat

__module_name__ = "updown.py"

__module_version__ = "0.0.1"

__module_author__ = "ComputerTech"

__module_description__ = "Manage your access on the current channel"

def isop():

	me = hexchat.get_info("nick")	for u in hexchat.get_list("users"):

		if u.nick == me:

			if '@' in u.prefix:

				return True

			else:

				return False

def up(word, word_eol, userdata):

	chan = hexchat.get_info('channel')

	if not chan.startswith('#'):

		print("This command must be used in a channel window.")

		return hexchat.EAT_ALL

	if isop():

		print("You're already Op'd in", chan)

		return hexchat.EAT_ALL

	hexchat.command("msg chanserv OP", chan)

hexchat.hook_command('up', up, help="Ops you with chanserv in the current channel, if you are not already.")

hexchat.hook_command('down', down, help="Ops you with chanserv in the current channel, if you are not already.")

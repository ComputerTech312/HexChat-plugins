import hexchat

__module_name__ = 'Zap'
__module_author__ = 'ComputerTech'
__module_version__ = '0.1'
__module_description__ = 'ZAP!'

def isop():
	me = hexchat.get_info("nick")
	for people in hexchat.get_list("users"):
		if people.nick == me:
			if '@' in u.prefix:
				return True
			else:
				return False
    
def oop(word, word_eol, userdata):
	chan = hexchat.get_info("channel")
	if isop():
		print("You're already op'd in", chan)
		return hexchat.EAT_ALL
	hexchat.command("cs OP " + chan)
  
hexchat.hook_command('oop', oop, help="Gives you Op via chanserv")
hexchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded')

import hexchat

__module_name__ = 'Xline'
__module_author__ = 'ComputerTech'
__module_version__ = '0.1'
__module_description__ = 'A simple Gline script.'

def ctgline(word, word_eol, userdata):
  target = word[1]
  hexchat.command(f'GZLINE {target} 1d Banned')
  
hexchat.hook_command('xline', icycle)
hexchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded')
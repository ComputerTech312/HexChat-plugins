import hexchat

__module_name__ = 'Xline'
__module_author__ = 'ComputerTech'
__module_version__ = '0.1'
__module_description__ = 'A simple Network ban script.'

def xline(word, word_eol, userdata):
  target = word[1]
  hexchat.command(f'GZLINE {target} 1d Change reason here')
  
hexchat.hook_command('xline', xline)
hexchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded')

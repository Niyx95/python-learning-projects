#!/usr/bin/env python3
import sys, pyperclip
from deep_translator import GoogleTranslator

#get sys argument or copied text
if len(sys.argv) > 1:
    word = ''.join(sys.argv[1:])
else:
    word = pyperclip.paste()

#call google translator 
translate = GoogleTranslator(source='english', target='italian',).translate(word)

#print out result 
print(f'{word} is translated in {translate}')

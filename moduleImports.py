# Modules must be imported before use
# Some modules are included by default
import random, sys, os, math

print(random.randint(1, 10))

# Many modules can be installed from the command 
# line using pip
import pyperclip

pyperclip.copy('Hello World')
print(pyperclip.paste())

sys.exit()
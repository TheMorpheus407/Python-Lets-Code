import pymem
import os
import subprocess

notepad = subprocess.Popen(['notepad.exe'])

mem = pymem.Pymem('notepad.exe')
mem.inject_python_interpreter()
path = os.path.join(os.path.abspath('audio'), 'injected.txt')
path = path.replace("\\", "\\\\")
shellcode = """
f = open("{}", "w+")
f.write("Hello I'm injected")
f.close()
""".format(path)
mem.inject_python_shellcode(shellcode)

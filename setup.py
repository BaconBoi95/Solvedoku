import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python37-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python37-32\\tcl\\tk8.6"

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executabless = [
    Executable('Solvedoku.py', base=base)
]
optionss = {
    'build_exe': {
        'include_files':[
            'C:\\Program Files (x86)\\Python37-32\\DLLs\\tk86t.dll',
            'C:\\Program Files (x86)\\Python37-32\\DLLs\\tcl86t.dll'
        ]
    }
}

setup(name='SolveDoku',
      version='1.0.1.1',
      description='Solve Sudoku Easily',
      executables=executabless,
      author = "Matt Patterson",
      author_email = "leeland230.fun@gmail.com",
      options = optionss
      )

import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "sys", "tkinter"]}

base = "Win32GUI"

setup(  name = "NoteVelocity",
        version = "0.5",
        description = "A speedy note-taking and revision program",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])

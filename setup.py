from cx_Freeze import setup, Executable

setup(name="Random array reorder", executables=[Executable("Random array reorder script.py")], options={"build_exe": {"excludes": ["tkinter"]}})

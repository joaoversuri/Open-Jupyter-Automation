import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["pyautogui"]}

base = None
if sys.platform == "Win32":
    base = "Win3GUI"

setup(
    name='OpenJupyter',
    version='1.0',
    description='Open Jupyter Notebook',
    author="João Versuri",
    options={'build_exe': build_exe_options},
    executables=[Executable('open_jupyter.py', base=base, icon="jupyter_app_icon.ico")]
)
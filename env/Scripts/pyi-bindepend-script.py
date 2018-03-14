#!"c:\users\series 9\desktop\ppl2\ppl2018-c7\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'PyInstaller==3.3','console_scripts','pyi-bindepend'
__requires__ = 'PyInstaller==3.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PyInstaller==3.3', 'console_scripts', 'pyi-bindepend')()
    )

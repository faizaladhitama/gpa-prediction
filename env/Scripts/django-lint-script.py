#!"c:\users\series 9\desktop\ppl2\ppl2018-c7\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'django-lint==2.0.4','console_scripts','django-lint'
__requires__ = 'django-lint==2.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('django-lint==2.0.4', 'console_scripts', 'django-lint')()
    )

import shutil
import os
from pathlib import Path
import subprocess
packages = ['pre-commit']

# Виконати команду pip для кожного пакета
for package in packages:
    subprocess.check_call(['pip', 'install', package])

file_path = 'pre-commit/pre-commit'

if os.path.isfile(file_path):
        src = 'pre-commit/pre-commit'
        dst = '.git/hooks'
        shutil.move(src, dst)
        print("git-leaks enabled")
else:
        src = '.git/hooks/pre-commit'
        dst = 'pre-commit/'
        shutil.move(src, dst)
        print("git-leaks disabled")


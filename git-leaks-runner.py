import shutil
import os
from pathlib import Path
import importlib
import subprocess

def install_package(package_name):
    try:
        importlib.import_module(package_name)
        print(f"Package '{package_name}' is already installed.")
    except ImportError:
        subprocess.check_call(['pip', 'install', package_name])
        print(f"Package '{package_name}' has been installed.")

# Пакет, який потрібно встановити
package_name = 'pre-commit'

# Виконати встановлення пакета тільки у випадку його відсутності
install_package(package_name)

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


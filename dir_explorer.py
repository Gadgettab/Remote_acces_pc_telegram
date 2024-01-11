import getpass
import os
from aiogram.types.input_file import FSInputFile

default_location = fr"{os.getcwd()}\testDir"
print(default_location)

def set_default():
    os.chdir(default_location)


def get_dir_content():
    return os.listdir()


def move_to(dir):
    if os.path.isdir(dir):
        os.chdir(os.getcwd()+rf"\{dir}")
    else:
        return "Dir error"


def return_to_prev():
    if os.getcwd() != default_location:
        os.chdir("..")
        return os.getcwd()
    else:
        return "Dir limit reached"


def get_file(file):
    return FSInputFile(file)


set_default()

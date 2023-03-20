import os
import sys
import subprocess
from tkinter import filedialog

import byte_converter


class Element:
    def __init__(self, path, size):
        self.path = path
        self.size = size
        self.name = os.path.split(path)[1]

    def __str__(self):
        size_tuple= byte_converter.convert_byte(self.size)
        size_str = f"{size_tuple[0]}{size_tuple[1]}"
        return f"{self.name}  {size_str}"


# this return element size for sorting elements
def element_size(element):
    return element.size

def print_elements(list):
    print(end="\n" * 3)
    for i in range(len(list)):
        print(f"{i} {list[i]}")



def run(path):
    # creating directory list with elements whole paths
    dir_list = [os.path.join(path, x) for x in os.listdir(path)]
    if len(dir_list) == 0:
        print("This directory is empty!")
        return 0
    # looping through every file and folder in list and creating element objects of them and append to elements
    elements = []
    for file_folder_path in dir_list:
        if os.path.isfile(file_folder_path):
            elements.append(Element(file_folder_path, os.path.getsize(file_folder_path)))
        else:
            size = 0
            for dirpath, dirnames, filenames in os.walk(file_folder_path):
                for file in filenames:
                    size += os.path.getsize(os.path.join(dirpath, file))
            elements.append(Element(file_folder_path, size))

    # sorting elements from min size to max size
    elements.sort(key=element_size)

    # printing every element
    print_elements(elements)

    # choosing action (show in finder or quit the program)
    while True:
        action = input(f"[0-{len(elements)-1}: show in finder, q: quit]\n$ ")
        if action.isnumeric():
            action = int(action)
            if action in range(len(elements)):
                subprocess.call(["open", "-R", elements[action].path])
        else:
            action = action.lower()
            if action in ["q", "quit", "exit"]:
                break
            elif action in ["r", "renew", "reload", "refresh"]:
                dir_list = os.listdir(path)
                for element in elements:
                    if element.name not in dir_list:
                        elements.remove(element)
                print_elements(elements)


# if program executed with argument
if len(sys.argv) > 1:
    # if argument is a legit path
    if os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
        run(path)
    else:
        print("Error: There is no such directory!")
else:
    path = filedialog.askdirectory()
    run(path)








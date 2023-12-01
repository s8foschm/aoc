# ADVENT OF CODE 2022
# https://adventofcode.com/
# Day 7
# Francesco Georg Schmitt
# https://github.com/s8foschm/aoc2022

import re

# Global variables
directory_sizes = {}
directory_contents = {}
files = {}
total_size = 70000000
necessary_size = 30000000


def parse_command(lines, index, line, working_directory):
    if re.match("^[$] cd", line):
        target = parse_cd(lines, index, line)
        working_directory = change_directory(working_directory, target)
        # print("cd", working_directory)
        return working_directory
    elif re.match("^[$] ls", line):
        contents = parse_ls(lines, index, line)
        # print("ls", contents)
        directory_contents[working_directory] = contents
        return working_directory
        # directory_sizes[working_directory] = find_directory_size(contents)


def parse_ls(lines, index, line):
    contents = []
    index = index + 1
    line = lines[index]
    while (True):
        contents.append(line[:-1])
        index = index + 1
        line = lines[index]
        if line[0] == "$":
            break
        elif line == "" or line == "\n":
            break
    return contents


def parse_cd(lines, index, line):
    target = line[5:]  # remove command
    if target[-1] == "\n":
        target = target[:-1]  # remove \n
    return target


def get_files_size(contents):
    size = 0
    for element in contents:
        if (re.match("^[0-9]* ", element)):
            size = size + int(element.split(' ')[0])
    return size


def get_subdirectories(contents, working_directory):
    subdirectories = []
    for element in contents:
        if (re.match("^dir ", element)):
            if working_directory != "/":
                subdirectories.append(working_directory + "/" + element[4:])
            else:
                subdirectories.append(working_directory + element[4:])
    return subdirectories


def get_directory_size(directory):
    size = get_files_size(directory_contents[directory])
    subdirectories = get_subdirectories(directory_contents[directory], directory)
    for subdirectory in subdirectories:
        size = size + get_directory_size(subdirectory)
    return size


def change_directory(curr_directory, target_directory):
    if target_directory[0] == "/":  # absolute path
        return target_directory
    elif target_directory == "..":  # parent directory
        if curr_directory == "/":
            raise ValueError("cannot go to parent directory of root directory", working_directory)
        else:
            directory_list = curr_directory.split("/")
            directory_list.pop(0)
            directory_list.pop()
            return "/" + "/".join(directory_list)
    else:  # regular cd
        if curr_directory[-1] == "/":
            return curr_directory + target_directory
        else:
            return curr_directory + "/" + target_directory


# ========== PART ONE ==========
def pretty_print(directory_sizes):
    total = 0
    for directory in directory_sizes:
        if directory_sizes[directory] <= 100000:
            total = total + directory_sizes[directory]
    print("Total sum:", total)


# ========== PART TWO ==========
def sort_directories(directory_sizes):
    return sorted(directory_sizes.items(), key=lambda kv: (kv[1], kv[0]))


with open('input.txt', 'r') as file:
    working_directory = "/"
    lines = file.readlines()

    # PARSE INPUT
    for (index, line) in enumerate(lines):
        if line[0] == "$":
            working_directory = parse_command(lines, index, line, working_directory)
        elif line == "":
            break
    print(directory_contents)

    for directory in directory_contents.keys():
        directory_sizes[directory] = get_directory_size(directory)
    print(directory_sizes)

    # PART ONE
    pretty_print(directory_sizes)

    # PART TWO
    occupied = directory_sizes['/']
    free = total_size - occupied
    to_be_freed = necessary_size - free
    sorted_directories = sort_directories(directory_sizes)
    for (directory, size) in sorted_directories:
        if size > to_be_freed:
            print(directory, size)
            break

import sys
import os


def check_file(filename: str) -> list:
    """
    The function checks whether specified file exists and if it
    does, it will split the lines into a list and return it. If
    it doesn't exist, it will write an error message saying
    the file doesn't exist.
    :param filename: The name of the specified file
    :return: list
    """
    line_list = list()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                line_list.append(line.split(", "))
        return line_list
    else:
        sys.stderr.write("Error: " + filename + " does not exist!")
        exit()

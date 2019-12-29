#!/usr/bin/python3


def read_from_file(path):
    """Read sudoku from a file and return an array
    """
    array = list()
    f = open(path, "r")
    for line in f:
        for c in line:
            if c.isdecimal():
                array.append(int(c))
            else:
                array.append(None)
    return array


def read_from_db():
    """Read sudoku from database and return an array
    """
    pass


def read_from_image():
    """Read sudoku from an image and return an array
    """
    pass


def read_from_scanner():
    """Read sudoku from camera and return an array
    """
    pass

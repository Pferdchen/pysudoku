#!/usr/bin/python3

# Open a file
path = "../templates/template1.txt"
fo = open(path, "r")
str = fo.read()
print ("Sudoku template:\n", str)

# Close opened file
fo.close()

print ("Sudoku result:\n", str)
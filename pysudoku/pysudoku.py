#!/usr/bin/python3

# Open a file
path = "../templates/template1.txt"
fo = open(path, "r")
sudoku_str = fo.read()
print("Sudoku template:\n", sudoku_str)

# Read sudoku_str into [][]...
for line in sudoku_str.split('\n'):
    print(list(line))

# Close opened file
fo.close()

print("Sudoku result:\n", sudoku_str)

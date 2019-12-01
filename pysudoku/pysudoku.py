#!/usr/bin/python3

# Open a file
path = "../templates/template1.txt"
fo = open(path, "r")
sudoku_str = fo.read()
print("Sudoku template:\n" + sudoku_str)

# Close opened file after usage
fo.close()

# init sudoku_matrix
sudoku_matrix = list()
for line in sudoku_str.split('\n'):
    sudoku_row = list()
    for c in list(line):
        if c.isdecimal():
            sudoku_row.append(int(c))
        else:
            sudoku_row.append(0)
    sudoku_matrix.append(sudoku_row)

# init suggestion_sets
suggestion_sets = list()
FULL_SUGGESTIONS = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in range(9):
    suggestion_row = list()
    for j in range(9):
        n = sudoku_matrix[i][j]
        if n != 0:
            suggestion_row.append(set([n]))
        else:
            suggestion_row.append(FULL_SUGGESTIONS.copy())
    suggestion_sets.append(suggestion_row)

print(suggestion_sets)

# recursive reduce
for i in range(9):
    for j in range(9):
        n = sudoku_matrix[i][j]
        if n!= 0:
            continue
        else:
            #TODO
            continue


#print("Sudoku result:\n" + sudoku_str)

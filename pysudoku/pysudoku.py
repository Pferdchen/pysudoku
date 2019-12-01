#!/usr/bin/python3


def reduce_sets(suggestion_sets, sudoku_matrix, i, j):
    possible_set = suggestion_sets[i][j]
    if len(possible_set) == 1 and sudoku_matrix[i][j] == 0:
        find = possible_set.pop()
        sudoku_matrix[i][j] = find
        possible_set.add(find)  # restore popped number in set
        reduce_sets_on_axis(suggestion_sets, sudoku_matrix, i, j)
        reduce_sets_in_square(suggestion_sets, sudoku_matrix, i, j)


def reduce_sets_on_axis(suggestion_sets, sudoku_matrix, i, j):
    for k in range(9):
        if k != j and len(suggestion_sets[i][k]) > 1:
            suggestion_sets[i][k].discard(sudoku_matrix[i][j])
            reduce_sets(suggestion_sets, sudoku_matrix, i, k)
        if k != i and len(suggestion_sets[k][j]) > 1:
            suggestion_sets[k][j].discard(sudoku_matrix[i][j])
            reduce_sets(suggestion_sets, sudoku_matrix, k, j)


def reduce_sets_in_square(suggestion_sets, sudoku_matrix, i, j):
    for r in range((i // 3) * 3, (i // 3) * 3 + 3):
        for s in range((j // 3) * 3, (j // 3) * 3 + 3):
            if r != i and s != j and len(suggestion_sets[r][s]) > 1:
                suggestion_sets[r][s].discard(sudoku_matrix[i][j])
                reduce_sets(suggestion_sets, sudoku_matrix, k, j)


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
        num = sudoku_matrix[i][j]
        if num != 0:
            suggestion_row.append(set([num]))
        else:
            suggestion_row.append(FULL_SUGGESTIONS.copy())
    suggestion_sets.append(suggestion_row)

#print(suggestion_sets)

# recursive reduce
for i in range(9):
    for j in range(9):
        num = sudoku_matrix[i][j]
        if num != 0:
            continue
        else:
            possible_values = suggestion_sets[i][j]
            for k in range(9):
                if k != j:
                    possible_values.discard(sudoku_matrix[i][k]) # remove on horizontal
                if k != i:
                    possible_values.discard(sudoku_matrix[k][j]) # remove on vertical

            for r in range((i // 3) * 3, (i // 3) * 3 + 3):
                for s in range((j // 3) * 3, (j // 3) * 3 + 3):
                    if r != i and s != j:
                        possible_values.discard(sudoku_matrix[r][s]) # remove in square

            reduce_sets(suggestion_sets, sudoku_matrix, i, j)

result_str = "Sudoku result:\n"
for row in sudoku_matrix:
    for num in row:
        result_str += '{}'
        result_str = result_str.format(num)
    result_str += '\n'
print(result_str)

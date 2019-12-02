#!/usr/bin/python3


def read_template(path):
    fo = open(path, "r")
    template = fo.read()
    fo.close()
    return template


def init_sudoku(template):
    matrix = list()
    for line in template.split(LINE_FEED):
        row = list()
        for c in list(line):
            if c.isdecimal():
                row.append(int(c))
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def init_suggestion(matrix):
    suggestion = list()
    for i in range(9):
        row = list()
        for j in range(9):
            num = matrix[i][j]
            if num != 0:
                row.append(set([num]))
            else:
                row.append(FULL_SUGGESTIONS.copy())
        suggestion.append(row)
    return suggestion


def calculate(sudoku, suggestion):
    for i in range(9):
        for j in range(9):
            num = sudoku[i][j]
            if num != 0:
                continue
            else:
                possible_values = suggestion[i][j]
                for k in range(9):
                    if k != j:
                        possible_values.discard(sudoku[i][k])  # remove on horizontal
                    if k != i:
                        possible_values.discard(sudoku[k][j])  # remove on vertical

                x, y = square_position(i, j)
                for r in range(x, x + SQUARE_OFFSET):
                    for s in range(y, y + SQUARE_OFFSET):
                        if r != i and s != j:
                            possible_values.discard(sudoku[r][s])  # remove in square

                reduce_sets(sudoku, suggestion, i, j)


def reduce_sets(sudoku, suggestion, i, j):
    possible_set = suggestion_sets[i][j]
    if len(possible_set) == 1 and sudoku[i][j] == 0:
        find = possible_set.pop()
        sudoku[i][j] = find
        possible_set.add(find)  # restore popped number in set
        reduce_sets_on_axis(sudoku, suggestion, i, j)
        reduce_sets_in_square(sudoku, suggestion, i, j)


def reduce_sets_on_axis(sudoku, suggestion, i, j):
    for k in range(9):
        if k != j and len(suggestion[i][k]) > 1:
            suggestion[i][k].discard(sudoku[i][j])
            reduce_sets(sudoku, suggestion, i, k)
        if k != i and len(suggestion[k][j]) > 1:
            suggestion[k][j].discard(sudoku[i][j])
            reduce_sets(sudoku, suggestion, k, j)


def reduce_sets_in_square(sudoku, suggestion, i, j):
    x, y = square_position(i, j)
    for r in range(x, x + SQUARE_OFFSET):
        for s in range(y, y + SQUARE_OFFSET):
            if r != i and s != j and len(suggestion[r][s]) > 1:
                suggestion[r][s].discard(sudoku[i][j])
                reduce_sets(sudoku, suggestion, r, s)


def square_position(i, j):
    return (i // 3) * 3, (j // 3) * 3


# main begin
LINE_FEED = '\n'
SQUARE_OFFSET = 3
FULL_SUGGESTIONS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

sudoku_template = read_template("../templates/template1.txt")
print("Sudoku template:" + LINE_FEED + sudoku_template)

sudoku_matrix = init_sudoku(sudoku_template)
suggestion_sets = init_suggestion(sudoku_matrix)
# print(suggestion_sets)

calculate(sudoku_matrix, suggestion_sets)
# print(suggestion_sets)

sudoku_result = ""
for num_line in sudoku_matrix:
    for cell_num in num_line:
        sudoku_result += '{}'
        sudoku_result = sudoku_result.format(cell_num)
    sudoku_result += LINE_FEED
print("Sudoku result:" + LINE_FEED + sudoku_result)

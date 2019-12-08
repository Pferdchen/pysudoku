#!/usr/bin/python3


def read_template(file_name):
    with open(file_name) as file:
        return file.read()


def init_sudoku(template):
    matrix = list()
    for line in template.split(LINE_FEED):
        num_list = list()
        for c in line:
            if c.isdecimal():
                num_list.append(int(c))
            else:
                num_list.append(None)
        matrix.append(num_list)
    return matrix


def init_suggestion_sets(matrix):
    suggestion_matrix = list()
    for i in range(9):
        suggestion_set_list = list()
        for j in range(9):
            num = matrix[i][j]
            if num is not None:
                suggestion_set_list.append({num})
            else:
                suggestion_set_list.append(FULL_SUGGESTION.copy())
        suggestion_matrix.append(suggestion_set_list)
    return suggestion_matrix


def calculate(sudoku, suggestion):
    for i in range(9):
        for j in range(9):
            num = sudoku[i][j]
            if num is not None:
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
    possible_values = suggestion[i][j]
    if len(possible_values) == 1 and sudoku[i][j] is None:
        sudoku[i][j] = max(possible_values)  # only one possible value
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


def write_result(matrix):
    result = ""
    for num_list in sudoku_matrix:
        for n in num_list:
            result += '{}'
            if n is None:
                result = result.format(SPACE)
            else:
                result = result.format(n)
        result += LINE_FEED
    return result


# main begin
LINE_FEED = '\n'
SPACE = ' '
SQUARE_OFFSET = 3
FULL_SUGGESTION = {1, 2, 3, 4, 5, 6, 7, 8, 9}

path = "../templates/template1.txt"
sudoku_template = read_template(path)
print("Sudoku template:" + LINE_FEED + sudoku_template)

sudoku_matrix = init_sudoku(sudoku_template)
suggestion_sets = init_suggestion_sets(sudoku_matrix)
# print(suggestion_sets)

calculate(sudoku_matrix, suggestion_sets)
print(suggestion_sets)

sudoku_result = write_result(sudoku_matrix)
print("Sudoku result:" + LINE_FEED + sudoku_result)

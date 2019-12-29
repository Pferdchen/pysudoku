#!/usr/bin/python3


class Cell:
    FULL_SUGGESTIONS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self, result):
        """If the result is None, suggestions is a set of numbers.
        If the result is an unique number, suggestions is {result}.
        """
        self.result = result
        if result is None:
            self.suggestions = Cell.FULL_SUGGESTIONS.copy()
        else:
            self.suggestions = {result}


class Sudoku:
    def __init__(self, temp_array):
        self.solution = list()  # 9*9 cells
        self.rows = list()  # 9 rows, each 9 cells
        for i in range(9):
            self.rows.append(list())
        self.columns = list()  # 9 columns, each 9 cells
        for i in range(9):
            self.columns.append(list())
        self.regions = list()  # 9 regions, each 9 cells
        for i in range(9):
            self.regions.append(list())
        for i in range(81):
            cell = Cell(temp_array[i])
            self.solution.append(cell)
            self.rows[Sudoku.row_index(i)].append(cell)
            self.columns[Sudoku.column_index(i)].append(cell)
            self.regions[Sudoku.region_index(i)].append(cell)

    @staticmethod
    def row_index(i: int) -> int:
        return i // 9

    @staticmethod
    def column_index(i: int) -> int:
        return i % 9

    @staticmethod
    def region_index(i: int) -> int:
        return ((i // 9 // 3) * 3) + ((i % 9) // 3)

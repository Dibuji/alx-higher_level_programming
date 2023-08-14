#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = ""
        for element in row:
            row_str += "{:d} ".format(element)
        print(row_str.strip())

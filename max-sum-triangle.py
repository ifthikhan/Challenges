#!/usr/bin/env python


def get_triangle():
    #triangle = [
        #[3],
        #[7, 4],
        #[2, 4, 6],
        #[8, 5, 9, 3]
    #]
    #return triangle
    triangle = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 04, 82, 47, 65],
        [19, 01, 23, 75, 03, 34],
        [88, 02, 77, 73, 07, 63, 67],
        [99, 65, 04, 28, 06, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
    ]
    return triangle


def calculate_max_sum(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        cur_row = triangle[i]
        row_below = triangle[i + 1]
        for i_cell in range(0, i + 1):
            cur_row[i_cell] += max(row_below[i_cell], row_below[i_cell + 1])
        triangle[i] = cur_row
    return triangle[0][0]


def calculalate_max_sum_recursive(triangle):
    if len(triangle) <= 1:
        return triangle[0]
    cur_row = triangle.pop(0)
    row_below = calculalate_max_sum_recursive(triangle)
    for i, cell in enumerate(cur_row):
        cur_row[i] = max(row_below[i], row_below[i + 1])
    return cur_row


if __name__ == '__main__':
    triangle = get_triangle()
    print "The maximum sum (iterative) is %d" % calculate_max_sum(triangle)
    print "The maximum sum (resursive) is %d" % calculalate_max_sum_recursive(triangle[0])
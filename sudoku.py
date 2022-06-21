from math import floor
sudoku = []
accumulator = []
Y, X, stop = 0, 0, 1

for _ in range(9):
    sudoku.append([int(i) for i in input()])

def free(y, x, cell):
    if cell in sudoku[y]:
        return False
    for i in range(9):
        if sudoku[i][x] == cell:
            return False
    s_y = floor(y / 3) * 3
    s_x = floor(x / 3) * 3
    for j in range(s_y, s_y + 3):
        for i in range(s_x, s_x + 3):
            if sudoku[j][i] == cell:
                return False
    return True


def delete(accumulator):
    if accumulator[-1][-1] == 9:
        sudoku[accumulator[-1][0]][accumulator[-1][1]] = 0
        del accumulator[-1]
        return delete(accumulator)
    else:
        return accumulator


def spin(Y, X, stop):
    if sudoku[Y][X] == 0:
        for cell in range(stop, 10):
            if free(Y, X, cell):
                sudoku[Y][X] = cell
                accumulator.append((Y, X, cell))
                return True
        else:
            return False
    else:
        return True


while True:
    if spin(Y, X, stop):
        if X < 8:
            X += 1
            stop = 1
        elif X == 8 and Y < 8:
            X = 0
            Y += 1
            stop = 1
        elif X == 8 and Y == 8:
            break
    else:
        if accumulator[-1][-1] == 9:
            accumulator = delete(accumulator)
        ex = accumulator.pop()
        sudoku[ex[0]][ex[1]] = 0
        Y, X, stop = ex[0], ex[1], ex[2] + 1


for i in range(9):
    print("".join(str(j) for j in sudoku[i]))
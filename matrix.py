from random import randint
matrix = []
for i in range(5):
    subMatrix = []
    for j in range(5):
        subMatrix.append(randint(0,5))
    matrix.append(subMatrix)

for _ in matrix:
    print(_)

matrix =[
    [0, 5, 1, 5, 5],
    [1, 4, 5, 5, 1],
    [5, 5, 2, 2, 5],
    [1, 3, 2, 1, 2],
    [4, 3, 3, 2, 4]]
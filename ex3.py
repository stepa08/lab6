matrix = [
    [1, 2, 4],
    [4, 5, 6],
    [7, 8, 9],
]

transposed = [list(row) for row in zip(*matrix)]

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nТранспонированная матрица:")
for row in transposed:
    print(row)
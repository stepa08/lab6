matrix = [
    [1, 2, 4],
    [4, 5, 6],
    [7, 8, 9],
]

transposed = [list(row) for row in zip(*matrix)] # Создаем транспонирование

print("Исходная матрица:") # Заголовок исходной матрицы
for row in matrix: # Цикл по строкам матрицы
    print(row)

print("\nТранспонированная матрица:") # Заголовок транспонированной матрицы
for row in transposed: # Цикл по строкам результата
    print(row)
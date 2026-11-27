try:
    n = int(input("Введите количество элементов списка: "))
    m = []
    for i in range(n):
        print(f"Элемент: {i+1}")
        a = int(input("Введите элемент: "))
        m.append(a)
    b = sorted(m)
    if b == m:
        print("Список отсортирован")
    else:
        print("Список не отсортирован")
except ValueError:
    print("Это не число")
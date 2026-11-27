import random

n = int(input("Введите N: ")) # запрашиваем размер списка
numbers = [random.randint(1,100) for _ in range(n)] # Генерация списка случайных чисел

print(f"Исходный список: {numbers}")
print(f"Сумма: {sum(numbers)}")
print(f"Среднее: {sum(numbers) / len(numbers):.2f}")
print(f"Минимум: {min(numbers)}")
print(f"Максимум: {max(numbers)}")

numbers.sort() # Сортировка списка по возрастанию
print(f"Отсортированный: {numbers}")

unique = list(dict.fromkeys(numbers)) # Удаление дубликатов с сохранением порядка
print(f"Без дубликатов: {unique}")

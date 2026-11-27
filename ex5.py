list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

union = set1 | set2 # находим объединение двух множеств
intersection = set1 & set2 # Находим пересечение двух множеств
difference = set1 - set2 # Вычисляем разность двух множеств

print(f"Обьединение: {sorted(union)}")
print(f"Пересеченние: {sorted(intersection)}")
print(f"Разность: {sorted(difference)}")

# Создаем объединение с сохранением порядка
union_ordered = list1 + [x for x in list2 if x not in list1]
# Создаем пересечение с сохранением порядка
intersection_ordered = [x for x in list1 if x in list2]

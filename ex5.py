list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

print(f"Обьединение: {sorted(union)}")
print(f"Пересеченние: {sorted(intersection)}")
print(f"Разность: {sorted(difference)}")

union_ordered = list1 + [x for x in list2 if x not in list1]
intersection_ordered = [x for x in list1 if x in list2]

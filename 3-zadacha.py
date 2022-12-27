#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный код: {lst}")
set_res = set(lst)
lst_res =(list(set_res))
print("Неповторяющиеся элементы: ")
for item in lst_res:
    print(item)

# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]

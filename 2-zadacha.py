# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


num = int(input("Введите число N: "))
i = 2 
lst = []
old = num

while i <= num:
    if num % i == 0:
        lst.append(i)
        num//= i
        i = 2
    else:
        i+=1
print(f" Для N = {old} -> {lst}")

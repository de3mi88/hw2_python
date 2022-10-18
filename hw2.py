from os import system
system('cls')

# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).

# float_num = input('input float number: ')
# # print(type(float_num))
# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print(sum)


# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')

# 3. Задайте список из n чисел 
# последовательности (1+\frac 1 n)^n и выведите на экран их сумму.

#n = int(input('Enter number: ')) 

#def sequence(n):
#    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   

#print(sequence(n))
#print(round(sum(sequence(n))))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 

#from random import randint
#numbers = []
#for i in range(10):
#    numbers.append(randint (-10,10))
#print(numbers)
#
#def get_numbers(numbers):
#    count =0 
#    for element in numbers:
#        count +=1
#    return count
#print('Number of elements: ', get_numbers(numbers))

#x = int(input('Enter  position of first element: '))
#y = int(input('Enter position of second element: '))

#for i in range(len(numbers)):
#    mult = numbers[x -1]*numbers[y - 1]
#print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)

# 5. Реализуйте случайное перемешивание списка.

#list = ['Веселый пианист', 250, 3.14, 'True ']
#print(list) 
#import random
#random.shuffle(list)
#print('->', list) 


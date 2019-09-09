'''1. Найдите произведение самого большого и самого маленького элементов списка. Так же, отобразате найденые элементы.'''

lst = (input()).split()
print('Произведение самого большого и самого маленького элементов списка', min(lst) + max(lst),
      'Минимальное число', min(lst), 'Максимальное число', max(lst), sep='\n')

'''2. Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество'''

from random import randint
lst = [randint(1, 101) for _ in range(10)]
count = 0
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        lst[i] = 0
        count += 1
print(lst, count)

'''3. Заполните список случайными числами и выполните реверс для части списка между элементами с индексами `a` и `b` (включая эти элементы)'''

from random import randint
lst = [randint(1, 101) for _ in range(10)]
a = int(input('Введите индекс первого элемента (от 0 до 9): '))
b = int(input('Введите индекс второго элемента (от 0 до 9): '))
c = lst[a:b + 1]
d = lst[:a] + c[::-1] + lst[b + 1:]
print(lst, d, sep='\n')

'''4. Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000, и возвращающую `True`, если оно простое, и
`False` - иначе.'''

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True

print(isPrime(79))

'''5. Написать функцию `is_date`, принимающую 3 аргумента — день, месяц и год. Вернуть `True`, если дата корректная (надо
учитывать число месяца. Например 30.02 - дата не корректная, так же 31.06 или 32.07 и т.д.), и `False` иначе.'''

def is_date(year, month, day):
    import datetime
    try:
        d = datetime.date(year, month, day)
        return True
    except ValueError:
        return False

print(is_date(2019, 11, 3))
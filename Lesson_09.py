'''1.Написать следующие выражения:
- (a + b * c)
- a - 4 * b / c
- (a * b + 4) / (c -  1)'''

a = int(input('Введите число "а": '))
b = int(input('Введите число "b": '))
c = int(input('Введите число "c": '))
print('a + b * c =', a + b * c)
print('a - 4 * b / c =', a - 4 * b / c)
print('(a * b + 4) / (c - 1) =', (a * b + 4) / (c - 1))

'''2.	Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры'''

n = input('Введите пятизначное число: ')
sum = 0
for i in n:
    if int(i) % 2 != 0:
        sum += int(i)
print("Сумма нечётных цифр:", sum)

'''3.	Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из 
моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло 
между двумя моментами времени. Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый 
момент времени и три целых числа, задающих второй момент времени. Выведите число секунд между этими моментами времени.'''

a = (input('Введите три целых числа: часы, минуты, секунды: ')).split()
b = (input('Введите три целых числа: часы, минуты, секунды: ')).split()
a = [int(i) for i in a]
b = [int(i) for i in b]
print('Разница между интервалами в секундах: ', ((b[0] - a[0]) * 3600) + ((b[1] - a[1]) * 60) + (b[2] - a[2]))


'''4.	Определить является ли строка [изограммой](https://en.wikipedia.org/wiki/Isogram ), т.е. что все буквы в ней за 
исключением пробелов встречаются только один раз. Например, строки 'Питон', 'downstream', 'книга без слов' являются 
изограммами, а само слово 'изограмма' - нет.'''

txt = input('Введите строку(и) для проверки на изограммы: ').split()
a = ''.join(txt)
if len(set(a)) == len(a):
    print('Данная строка является изограммой')
else:
    print('Данная строка не является изограммой')


'''5.	Дано целое, положительное **ЧИСЛО** (не строка). Необходимо его перевернуть (**работаем как с ЧИСЛОМ**). Программа 
принимает на вход целое число, возвращает **ЧИСЛО** являющееся зеркальным отражением исходного. **Нечего, кроме, цикла 
и арифметических операторов применять нельзя**.'''

number = int(input('Введите целое, положительное число: '))
reverse = 0
while number != 0:
    reverse = number % 10
    number = number // 10
    print(reverse, end='')

'''6.	В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах. 
**Новый список создавать нельзя!**'''

lst = list(input('Веедите любые числа в список: '))
a = lst.index(max(lst))
b = lst.index(min(lst))
if a > b:
    lst[a], lst[b] = lst[b], lst[a]
print('Список, в котором поменяли местами минимальный и максимальный элементы', lst)

'''7.	Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к интервалу 
от -1 до 1, причем максимальное абсолютное значение элементов после нормирование должно быть равно 1. Например, 
последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]'''

from random import randint

lst = [randint(-10, 10) for _ in range(10)]
a = abs(max(lst, key=abs))
b = [(element/a) for element in lst]
print(lst, b, end='')

'''8. Дан список. Необходимо его перевернуть. Использовать срезы, метод revers() и подобные встроенные механизмы, а так же
оператор IF **ЗАПРЕЩЕНО**. Можно использовать **только** цикл и арифметические операторы!'''

lst = list(input('Веедите любые числа в список: '))
a = lst.index(max(lst))
b = lst.index(min(lst))
while a > b:
    lst[a], lst[b] = lst[b], lst[a]
    a -= 1
    b += 1
print(lst)

'''9. Дан список целых чисел, индекс `k` и значение `C`. Необходимо вставить в список на позицию с индексом `k` значение 
`C`, сдвинув все элементы, имевшие индекс не менее `k`, вправо. Поскольку при этом количество элементов в списке 
увеличивается, необходимо, перед сдвигом, увеличить список на один элемент, используя метод append().
	- Вставку необходимо осуществлять уже в расширеный списк, не создавая дополнительного списка.
	- Использовать метод `insert()` не **разрешается**.
	- Допустимо использовать `append()`, цикл, `range()` и оператор индексирования.'''

from random import randint

k = int(input('Выбирите индекс числа (от 0 до 10): '))
C = int(input('Введите само число: '))
lst = [randint(0, 5) for _ in range(10)]
lst.append(k)
for i in range(len(lst), k):
    lst[i] = lst[i - 1]
lst[k] = C
print(lst)

'''10.	Используя циклы и оператор `IF` написать функции для построения фигур изображеных на рисунке ниже. Функции принимают 
в качестве аргумента высоту фигуры в символах и на основании этого строят фигуры.
![ресунке](img/rhombus.png)'''
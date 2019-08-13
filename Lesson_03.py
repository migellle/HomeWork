'''1. Длина маршрута велоралли "100 километров за 10 часов по Поясу Славы" - примерно 100 километров. Велосипедист Вася
стартует с нулевого километра маршрута и едет со скоростью `v` километров в час. На какой отметке он остановится через
`t` часов?
Программа получает на вход значение `v` и `t`. Если `v > 0`, то Вася движется в положительном направлении по маршруту,
если же значение `v < 0`, то в отрицательном.
Программа должна вывести целое число от 0 до 100 — номер отметки, на которой остановится Вася.'''

v = int(input('Введите скорость движения в км\ч: '))
t = int(input('Введите количество потрачанных часов: '))
print(v * t % 100)


'''2. Дано положительное действительное (вещественное) число `X`.
    - Выведите его дробную часть.
    - Выведите его первую цифру после десятичной точки.'''

a = float(input('Введите вещественное число: '))
print(a - int(a))
print((a * 10) % 10)


'''3. Дано трехзначное число. Найдите сумму его цифр.'''

a = int(input('Введите трехзначное число: '))
b = a % 10
c = (a//10) % 10
d = (a//100) % 10
print(b + c + d)

'''4. В математике функция `sign(x)` (знак числа) определена так:
    ``
    sign(x) = 1, если x > 0,
    sign(x) = -1, если x < 0,
    sign(x) = 0, если x = 0.
    ``

    Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных
    инструкций if... elif... else.'''

sign(x) = int(input('Введите число x: '))
if x > 0:
    print('sign(x) > 0')
elif x == 0:
    print('sign(x) = 0')
else:
    print('sign(x) < -1')


number = float(input('Enter number: '))
if number > 0:
    print('sign(x) = 1')
elif number == 0:
    print('sign(x) = 0')
else:
    print('sign(x) = -1')

'''5. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является
високосным, то выведите `YES`, иначе выведите `NO`. Напомним, что в соответствии с григорианским календарем, год
является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.'''

a = int(input('Введите натуральное число для определения высокосного года: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("YES")
else:
    print("NO")


'''6. Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую
одним ходом.'''

x = int(input('Введите координаты x (где расположен конь, число от 1 до 8): '))
y = int(input('Введите координаты y (где расположен конь, число от 1 до 8): '))
x1 = int(input('Введите координаты x1 (куда походит конь, от 1 до 8): '))
y1 = int(input('Введите координаты y1 (куда походит конь, от 1 до 8): '))
movex = (x - x1)
movey = (y - y1)
if movex == 1 and movey == 2 or movex == 2 and movey == 1:
    print('Ход возможен')
elif movex == -1 and movey == 2 or movex == 2 and movey == -1:
    print('Ход возможен')
elif movex == -1 and movey == -2 or movex == -2 and movey == -1:
    print('Ход возможен')
elif movex == 1 and movey == -2 or movex == -2 and movey == 1:
    print('Ход возможен')
else:
    print('Ход невозможен')
# 1. Установить Python 3.x - Done
# 2. Установить PyCharm Community - Done
''' 3. Ввести в консоле
    a. import this
    b. import antigravity
    c. import __hello__
    d. from __future__ import braces'''

import this
import antigravity
import __hello__
'''from __future__ import braces - File "<input>", line 1
SyntaxError: not a chance'''

'''4. Вывести на консоль своё имя, нарисованное 'звёздочками'

    *       *         *         *       * *********
    **      *        * *        **     ** *
    * *     *       *   *       * *   * * *
    *  *    *      *     *      *  * *  * *******
    *   *   *     *       *     *   *   * *
    *    *  *    ***********    *       * *
    *     * *   *           *   *       * *
    *      **  *             *  *       * *
    *       * *               * *       * **********'''

print('*\t\t\t\t  * * *********\t\t *\t\t\t*\t\t  * *\n *\t\t\t\t *  *\t  *\t\t\t* *\t\t\t*\t\t  * *\n  *\t\t\t\t*   *\t  *\t\t   *   *\t\t*\t\t  * *\n   *\t\t   *\t*\t  *\t\t  *\t\t*\t\t*\t\t  * *\n\t*\t\t  *\t\t*\t  *\t\t *\t\t *\t\t*\t\t  * *\n\t *\t\t *\t\t*\t  *\t\t***********\t\t*\t\t  * *\n\t  *\t\t*\t\t*\t  *\t   *\t\t   *\t*\t\t  * *\n\t   *   *\t\t*\t  *   *\t\t\t\t*   *\t\t  * *\n\t\t* *\t\t\t*\t  *  *\t\t\t\t *  *\t\t  * *\n\t\t *\t\t\t*\t  * *\t\t\t\t  * ********* * *')
'''5. Написать программу, которая выводит в консоль таблицу Escape-последовательностей:

    Escape sequences
    \a      Bell (alert)
    \b      Backspace
    \n      New line
    \t      Horizontal tab
    \\      Backslash \
    \”      Double quotation mark “
    \’      Single quotation mark ‘ '''

a = (" \\a - Bell (alert)\n \\b - Backspace\n \\n - New line\n \\t - Horizontal tab\n \\ - Backslash \ \n \\” - Double quotation mark “\n \\’ - Single quotation mark ‘")
print(a)

'''6. Ввести с клавиатуры два целых числа: x и y
    - Вывести на экран консоли оба числа используя только один вызов print()
    - Вычислить сумму чисел
    - Выполнить целочисленное деление
    - Найти остаток
    - Вычислить степень числа: x^y'''

print('Choose a number for "x and y"')
x = int(input())
y = int(input())

print(x, y)
print(x + y)
print(x // y)
print(x % y)
print(x * y)

'''7. Напишите программу, которая считывает три числа и выводит их сумму и произведение. Каждое число записано в
отдельной строке.'''

print('Choose a number for "a, b, c"')
a = int(input())
b = int(input())
c = int(input())

print(a + b + c)
print(a * b * c)

'''8. Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
Каждое число записано в отдельной строке. (S = 1 / 2 * K1 * K2)'''

print('Choose a number for "K1 and K2"')
K1 = int(input())
K2 = int(input())
S = 1 / 2 * K1 * K2

print(S)
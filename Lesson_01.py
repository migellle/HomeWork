# 1. Установить Python 3.x - Done
# 2. Установить PyCharm Community - Done
''' 3. Ввести в консоле
    a. import this
    b. import antigravity
    c. import __hello__
    d. from __future__ import braces
'''

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
    *       * *               * *       * **********
'''
print('*                 * * *********      *          *         * *')
print(' *               *  *     *         * *         *         * *')
print('  *             *   *     *        *   *        *         * *')
print('   *           *    *     *       *     *       *         * *')
print('    *         *     *     *      *       *      *         * *')
print('     *       *      *     *     ***********     *         * *')
print('      *     *       *     *    *           *    *         * *')
print('       *   *        *     *   *             *   *         * *')
print('        * *         *     *  *               *  *         * *')
print('         *          *     * *                 * ********* * *')

'''5. Написать программу, которая выводит в консоль таблицу Escape-последовательностей:

    Escape sequences
    \a      Bell (alert)
    \b      Backspace
    \n      New line
    \t      Horizontal tab
    \\      Backslash \
    \”      Double quotation mark “
    \’      Single quotation mark ‘
    '''

print('Hello\a')
print('Hello\b')
print('Hello\n')
print('Hello\t')
print('Hello\\')
print('Hello\'')
print('Hello\"')

'''
6. Ввести с клавиатуры два целых числа: x и y
    - Вывести на экран консоли оба числа используя только один вызов print()
    - Вычислить сумму чисел
    - Выполнить целочисленное деление
    - Найти остаток
    - Вычислить степень числа: x^y
'''
x = 5
y = 3

print(x, y)
print(x + y)
print(x // y)
print(x % y)
print(x ^ y)

'''7. Напишите программу, которая считывает три числа и выводит их сумму и произведение. Каждое число записано в
отдельной строке.'''

a = 12
b = 17
c = 25
print(a + b + c)
print(a * b * c)

'''8. Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
Каждое число записано в отдельной строке. (S = 1 / 2 * K1 * K2)'''

K1 = 3
K2 = 5
S = 1 / 2 * K1 * K2

print(S)
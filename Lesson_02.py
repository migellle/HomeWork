'''1. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому
школьнику? Сколько яблок останется в корзинке? Программа получает на вход числа `n` и `k` и должна вывести искомое
количество яблок (два числа).'''

print('Please enter an integer number: first for school boy, second for apples:')
n = int(input())
k = int(input())
x = k // n
y = k % n
print('Result is: ' + str(x), str(y))

'''2. Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные
часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
Учтите, что число n может быть больше, чем количество минут в сутках.'''

print('Please enter an integer number for time')
n = int(input())
x = n // 60
y = n % 60
z = x % 24
print('Result is: ' + str(z), str(y))

'''3. Напишите программу, которая приветствует пользователя, выводя слово `Hello`, введенное имя и знаки препинания
по образцу: `Hello Kitty!`'''

print('Please enter your name:')
print("'Hello " + input() + "!'")

'''4. Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
(пробелы важны!). Первая строка содержит следующее значение, а втора строка содержит предыдущее значение введёного
числа

        Please enter an integer number: 1234
        The next number for the number 1234 is 1235.
        The previous number for the number 1234 is 1233.

     or

        Please enter an integer number: 0
        The next number for the number 0 is 1.
        The previous number for the number 0 is -1.'''

print('Please enter an integer number:')
a = int(input())
print('The next number for the number',a, 'is', a+1)
print('The previous number for the number',a, 'is', a-1)

'''5. В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то 
же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть 
не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт 
чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из 
трех классов.'''

print('Please enter an integer number, three times, for indicate school boys:')
a = int(input())
b = int(input())
c = int(input())

s = a//2 + b//2 + c//2 + a%2 + b%2 + c%2

print(s)

print('Well done! :)')
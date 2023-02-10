# написать программу сравнения 2х чисел (больше или меньше) не используя никаких операторов
#
a = int(input('введите число a: '))
b = int(input('введите число b: '))

my_list = list()
my_list.append(a)
my_list.append(b)

my_list.sort()

print(f'{my_list[0]} меньше {my_list[1]}')


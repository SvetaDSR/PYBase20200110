# Запросить у пользователя целое число.
# Вывести число в представлении целого числа, вещественного числа, логического значения, строки.
# Запросить у пользователя ещё одно целое число.
# Выполнить операции + и * над всеми вариантами представления первого числа и второго числа, если они допустимы.

num_1 = input('Пожалуйста, введите целое число:')

print('''
Целое число:''', int(num_1))
print('Вещественное число:', float(num_1))
print('Логическое значение:', bool(num_1))
print('Строка:', str(num_1))


num_2 = input('''
Пожалуйста, введите еще одно целое число:''')

print('''
Результат сложения целых чисел:''', int(num_1) + int(num_2))
print('Результат сложения целого и вещественного чисел:', int(num_1) + float(num_2))
print('Результат сложения 1го целого числа и 2го логического значения:', int(num_1) + bool(num_2))
print('Результат сложения 2го целого числа и 1го логического значения:', bool(num_1) + int(num_2))
print('Результат объединения целого числа и строки: недопустимая операция')

print('Результат сложения вещественных чисел:', float(num_1)+float(num_2))
print('Результат сложения 1го вещественного числа и 2го логического значения:', float(num_1) + bool(num_2))
print('Результат сложения 2го вещественного числа и 1го логического значения:', bool(num_1) + float(num_2))
print('Результат объединения вещественного числа и строки: недопустимая операция')

print('Результат сложения логических значений:', bool(num_1) + bool(num_2))
print('Результат объединения логического значения и строки: недопустимая операция')

print('Результат объединения строк:', str(num_1) + str(num_2))

print('''
Результат умножения целых чисел:''', int(num_1) * int(num_2))
print('Результат умножения целого и вещественного чисел:', int(num_1) * float(num_2))
print('Результат умножения 1го целого числа и 2го логического значения:', int(num_1) * bool(num_2))
print('Результат умножения 2го целого числа и 1го логического значения:', bool(num_1) * int(num_2))
print('Результат умножения целого числа и строки: недопустимая операция')

print('Результат умножения вещественных чисел:', float(num_1) * float(num_2))
print('Результат умножения 1го вещественного числа и 2го логического значения:', float(num_1) * bool(num_2))
print('Результат умножения 2го вещественного числа и 1го логического значения:', bool(num_1) * float(num_2))
print('Результат умножения вещественного числа и строки: недопустимая операция')


print('Результат умножения логических значений:', bool(num_1) * bool(num_2))
print('Результат умножения логического значения и строки: недопустимая операция')

print('Результат умножения строк: недопустимая операция')

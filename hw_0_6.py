#Вычисление площади треугольника по формуле Герона
a = int(input('Введите длину первой стороны треугольника, см:'))
b = int(input('Введите длину второй стороны треугольника, см:'))
c = int(input('Введите длину третьей стороны треугольника, см:'))
p = (a+b+c)/2
triangle_area = (p*(p-a)*(p-b)*(p-c)) ** .5
print('Площадь треугольника равна', triangle_area,'см')
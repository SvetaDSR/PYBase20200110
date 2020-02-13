# Создать программу, решающую квадратное уравнение вида ax^2 + bx + c = 0
#
# Формула для корней квадратного уравнения: x1, 2 = (−b±√(b^2−4ac))/2a
#
# Пользователь должен по очереди ввести коэфициенты a, b, c.
# Если уравнение не имеет вещественных решений - вывести сообщение на экран и показать комплексные корни уравнения.
# Если уравнение имеет только один корень (вещественное число), то вывести сообщение об этом и показать значение.
# Если уравнение имеет два корня (вещественных чисел), то вывести сообщение об этом и показать оба значения.
# Необходимо обязательно вычислять и использовать Дискриминант.

# a = int(input('Пожалуйста, введите коэффициент a:'))
# b = int(input('Пожалуйста, введите коэффициент b:'))
# c = int(input('Пожалуйста, введите коэффициент c:'))

def quadratic_equation(a, b, c, x_1 = 0, x_2 = 0):
    D = b**2 - 4*a*c
    print(D)
    if D == 0:
        x_1 = -b / 2 * a
        x_2 = " "
    else:
        x_1 = (-b + D ** .5)/(a*2)
        x_2 = (-b - D ** .5)/(a*2)
        return x_1, x_2
    print(x_1, x_2)


print(quadratic_equation(int(input('Пожалуйста, введите коэффициент a:')),
                       int(input('Пожалуйста, введите коэффициент b:')),
                       int(input('Пожалуйста, введите коэффициент c:')))
      )

# Запросить у пользователя имя и фамилию.
# Поприветсвовать пользователя с использованием его имени и фамилии.
name_surname = input('Пожалуйста, введите Ваше Имя и Фамилию:')
print('''
Рады приветствовать Вас,''',name_surname,'!','''
''')

# Запросить День даты рождения.
# Запросить Месяц даты рождения.
# Запросить Год даты рождения.
birth_date = int(input('Пожалуйста, введите дату Вашего рождения в формате ДД:'))
birth_month = int(input('Пожалуйста, введите месяц Вашего рождения в формате ММ:'))
birth_year = int(input('Пожалуйста, введите год Вашего рождения в формате ГГГГ:'))

# Вывести количество прожитых лет.
if birth_date <= 31 and birth_month == 1:
    years = 2020 - birth_year
else:
    years = 2019 - birth_year
print('''
Количество прожитых Вами лет:''', years)

# Вывести количество прожитых месяцев.
if birth_month == 1:
    months = years*12
else:
    months = years*12 + (12 - birth_month)
print('Количество прожитых Вами месяцев:', months)

# Вывести количество прожитых дней, месяцев, лет до даты начала курса 10.01.2020 - без учёта високосных лет и среднее количество дней в месяце считать 30.
days = months*30 + 9
days_months_years = str(days) + ' дней /' + str(months) + ' месяцев /' + str(years) + ' лет.'
print('Количество прожитых Вами дней / месяцев / лет до даты начала курса 10.01.2020:', days_months_years)
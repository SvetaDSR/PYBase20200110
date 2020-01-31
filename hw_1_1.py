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


# Вывести количество прожитых месяцев.


# Вывести количество прожитых дней, месяцев, лет до даты начала курса 10.01.2020 - без учёта високосных лет и среднее количество дней в месяце считать 30.
num_days_in_1st_month_of_life = 30 - birth_date +1
num_passed_days_in_jan_2020 = 9
num_months_in_1st_year_of_life = 12 - birth_month +1
num_months_total = (2019 - birth_year)*12+num_months_in_1st_year_of_life
num_years_total = num_months_total // 12
num_days_total = (num_months_total - 1)*30 + num_days_in_1st_month_of_life + num_passed_days_in_jan_2020

days_months_years = str(num_days_total) + ' дней /' + str(num_months_total) + ' месяцев /' + str(num_years_total) + ' лет.'
print('Количество прожитых Вами дней / месяцев / лет до даты начала курса 10.01.2020:', days_months_years)
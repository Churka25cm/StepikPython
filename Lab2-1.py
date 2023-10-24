money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months_without_debt = 1

while money_capital >= spend:
    money_capital += salary  # Добавляем зарплату к подушке безопасности
    money_capital -= spend  # Вычитаем расходы
    spend += spend * increase  # Увеличиваем расходы на 5%
    months_without_debt += 1


print(f"Количество месяцев, которое можно протянуть без долгов: {months_without_debt}")

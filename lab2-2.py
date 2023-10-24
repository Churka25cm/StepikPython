salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0  # Изначально подушка безопасности равна нулю
total = 0
price_up = 0

for i in range(months):
    total += spend
    price_up = spend * increase
    spend += price_up
    money_capital = total - (salary * months)

money_capital = round(money_capital,2)


print("Необходимая подушка безопасности:", money_capital)

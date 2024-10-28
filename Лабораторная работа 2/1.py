money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # рост расходов
month = 0
while money_capital - spend + salary > 0:
	month += 1
	spend *= increase + 1
	money_capital += salary - spend

print("Количество месяцев, которое можно протянуть без долгов:", month)

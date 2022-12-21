deposit = 2130  # размер вклада
term = 5  # срок
percent = 10  # проценты
bonus = 120  # ежегодный бонус

result = deposit
year = 1

while year <= term:
    result = result + result * 0.1 + 120
    year += 1

print("Вклад", deposit, "руб. под", percent, "процентов с ежегодным бонусом", bonus, "руб. через", term, "лет будет равен", result)

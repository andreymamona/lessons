deposit = 2130
term = 5
percent = 10
bonus = 120

result = deposit
year = 1

while year <= term:
    result = result * 1.1 + 120
    year += 1

print(result)

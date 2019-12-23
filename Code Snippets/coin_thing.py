import math

money_owed = input()

quarters = math.floor(money_owed/25)
money_owed %= 25
dimes = math.floor(money_owed/10)
money_owed %= 10
nickels = math.floor(money_owed/5)
money_owed %= 5
pennies = money_owed

print("minimum coins required", quarters + dimes + nickels + pennies)

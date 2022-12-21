# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Выведите минимальное количество монет, которые нужно перевернуть.

import random
try:

    n = int(input("Введите число монет: "))
    coins = []
    for i in range(n):
        coins.append(random.randint(0,1))

    print(coins)
    heads = sum(coins)
    tails = n - heads

    if heads == 0 or tails == 0:
        print("Ничего переворачивать не нужно")
    elif heads > tails:
        print(f"Вам нужно перевернуть  {tails} монеток")
    else:
        print(f"Вам нужно перевернуть  {heads} монеток")
except:
    print("У вас нет монет, в следующий раз приходите с монетками!")

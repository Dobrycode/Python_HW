# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите длину шоколадки n= "))
m = int(input("Введите ширину шоколадки m= "))
k = int(input("Введите сколько нужно долек k= "))
while k > m * n:
    print("Введите другое количество долек!")
    n = int(input("Введите длину шоколадки n= "))
    m = int(input("Введите ширину шоколадки m= "))
    k = int(input("Введите сколько нужно долек k= "))
if k < m * n:
    if(k % m == 0 or k % n == 0):
        print("да! Можно отломить")
elif k == m * n:
        print("Это вся твоя долька")
else:
        print("Нельзя отломить столько долек")

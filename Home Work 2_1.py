#Задано n рядочків символів. Розробити програму, яка визначає і друкує окремо приголосні та
#голосні малі літери латинського алфавіту, які є в кожному рядку.
n = int(input("Введіть кількість рядків: "))
print("Введіть %d рядків!"%n)
strings = []
vowels = {'a','o','i','u','y','e'}
vow = set()
cons = set()
for i in range(n):
    strings.append(input())
for i in range(n):
    set_str = set(strings[i])
    for item in set_str:
        if item in vowels:
            vow.add(item)
        elif ord(item) >= 97 and ord(item) <= 122:
            cons.add(item)
    print("Vovels: ",vow,"  Consonants: ",cons)
    vow = set()
    cons = set()






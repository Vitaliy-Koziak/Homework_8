#Задано символьний рядок. Розробити програму, яка будує і друкує в алфавітному порядку
#множину малих, множину великих латинських літер, які містяться у заданому рядку, і
#множину цифр, яких немає у рядку.
str = input("Введіть рядок: ")
str = set(str)
set_of_lowercase = set()
set_of_uppercase = set()
set_of_notfound_numbers = set()
temp_set = set()
numbers = {'0','1','2','3','4','5','6','7','8','9'}
for item in str:
    if ord(item) >= 97 and ord(item) <= 122:
        set_of_lowercase.add(item)
    elif ord(item) >=65 and ord(item)<= 90:
        set_of_uppercase.add(item)
    elif ord(item) >=48 and ord(item)<= 57:
        temp_set.add(item)
set_of_notfound_numbers = numbers - temp_set
print(sorted(set_of_lowercase))
print(sorted(set_of_uppercase))
print(sorted(set_of_notfound_numbers))




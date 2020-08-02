#Задано два символьних рядка із малих і великих латинських літер та цифр. Розробити
#програму, яка будує і друкує в алфавітному порядку множину літер, які є в обох масивах, і
#множини літер окремо першого і другого масивів.
str1 = "acdfg98TRY"
str1_temp =''
str2 = "sFGHLM23gklx"
str2_temp =''

numbers = {'1','2','3','4','5','6','7','8','9','0'}
for item in str1:
    if item not in numbers:
        str1_temp+=item
for item in str2:
    if item not in numbers:
        str2_temp+=item
str1 = set(str1_temp)
str2 = set(str2_temp)
print(sorted(str1.union(str2)))
print(sorted(str1))
print(sorted(str2))
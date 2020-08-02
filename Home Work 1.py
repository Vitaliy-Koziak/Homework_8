#1)Створити список, що містить цифри, літери алфавіту (великі та малі), спеціальні символи;
#2)Розділити список на декілька, кожний з яких містить тільки цифри, тільки літери тощо;
#3)Конвертувати списки в кортежі;
#4)Ввести з клавіатури почергово цифру, літеру чи спецсимвол і повернути відповідно індекс входження у
#відповідний кортеж;
#5)Відобразити реверс одного з кортежів.
array = [3,5,4,'a','A','S','g','s','d','g',4,6,'d','^',8,9,2,'-','a','!','r','@','*','f','d',3,'@','s',2,0,'a','D','s',6,3,8,9,'H','D','%','F']
numbers = []
symbols = []
letters = []
for item in array:
    if type(item) == int:
        numbers.append(item)
    elif ((ord(item) >=65 and ord(item)<= 90) or (ord(item) >= 97 and ord(item) <= 122)) :
        letters.append(item)
    else:
        symbols.append(item)
numbers = tuple(numbers)
letters = tuple(letters)
symbols = tuple(symbols)
print("Tuple of numbers: ",numbers,'\n')
print("Tuple of letters: ",letters,'\n')
print("Tuple of symbols: ",symbols,'\n')
number = int(input("Enter a number: "))
letter = input("Enter a letter: ")
symbol = input("Enter a symbol: ")
print("Indexes of number %d in tuple of numbers:  "%number,end=" ")
for i in  range(len(numbers)):
    if numbers[i] == number:
        print(i,end="   ")
print()
print("Indexes of letter '%s' in tuple of letters:  "%letter,end=" ")
for i in  range(len(letters)):
    if letters[i] == letter:
        print(i,end="   ")
print()
print("Indexes of symbol '%s' in tuple of symbols:  "%symbol,end=" ")
for i in  range(len(symbols)):
    if symbols[i] == symbol:
        print(i,end="   ")
print('\n')
print("Reverse: ",end=" ")
print(tuple(reversed(symbols)))

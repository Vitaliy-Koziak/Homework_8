#Задано символьний рядок. Розробити програму, яка вилучає з цього рядка всі повторні
#входження цифр і знаків арифметичних операцій.
def Delete_repetitive(str, Arithmetic):
    str_temp = ''
    for item in str:
        if item.isdigit() or item in Arithmetic:
            if item in str_temp: pass
            else: str_temp += item
        else: str_temp += item
    return str_temp


def main():
    Arithmetic = ['+', '-', '*', '/']
    str = input("Enter string: ")
    print(Delete_repetitive(str, Arithmetic))

if __name__ == "__main__":
    main()
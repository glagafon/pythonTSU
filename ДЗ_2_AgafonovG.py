#Задание№1 
print("Задание №1")

units = ["Ноль","Один","Два","Три","Четыре","Пять","Шесть","Семь","Восемь","Девять"]
dozens = ["Десять","Двадцать","Тридцать","Сорок","Пятьдесят","Шестьдесят","Семьдесят","Восемьдесят","Девяносто"]

print("Введите число от 0 до 99")
a = True           #Булевая переменная для цикла while для отслеживания ошибки ValueError
#циклы для отлова ошибок 
try:
    number = int(input())
    while (int(number) < 0) or (int(number) > 99):
        print("Ошибка ввода")
        print("Введите число от 0 до 99")
        number = int(input())
except ValueError:
    a = False 
    print("Ошибка ввода")
    while a == False:
        print("Введите число от 0 до 99")
        try:
            number = int(input())
            a = True
        except ValueError:
            a = False
            print("Ошибка ввода")

str_number = ""     #Пустая строка (работает как пустой список) для заполнения ответами
b = 0 
''' 
b - вcпомогательная переменная для условия оператора elif.
Помогает не задействовать часть кода после оператора
'''
#цикл для конвертации чисел в буквы
for i in str(number):
    if len(str(number)) == 1:
        str_number+=str(units[int(i)])
    elif b == 0:
        str_number+=str(dozens[int(i)-1])
        b+=1
    else:
        str_number+=str(" ")
        str_number+=str(units[int(i)])

print(str_number)
        
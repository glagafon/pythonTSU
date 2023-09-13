from math import cos, sqrt
#Задание 1
print("Задание 1")
print("Введите сторону треуголька b")
b = float(input())
print("Введите сторону треуголька c")
c = float(input())
print("Введите угол между b и c")
beta = float(input())
while beta>=180:
    print("Угол должен быть меньше 180 градусов")
    print("Введите угол между b и c")
    beta = int(input())
def calculation(b,c,beta):
    return sqrt(b**(2)+c**(2)-2*b*cos(beta))
a = calculation(b,c,beta)
print("Третья сторона треугольника - ",float(a))
#Задание 2
print("Задание 2")
print("Введите температуру в градусах Цельсия")
C = float(input())
def calculation(C):
    return (9/5)*(C)+32
F = calculation(C)
print("Ваша температура в градусах Фаренгейта - ", F)
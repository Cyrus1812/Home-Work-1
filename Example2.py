# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math   
point1X = int(input("Введите первую координату первой точки: "))
point1Y = int(input("Введите вторую координату первой точки: "))
point2X = int(input("Введите первую координату второй точки: "))
point2Y = int(input("Введите вторую координату второй точки: ")) 
result = math.sqrt(math.pow((point2X - point1X),2)+ math.pow((point2Y - point1Y),2))
print(round(result,3))
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
import datetime
number = int(input("Введите число от 1 до 7: "))
now = datetime.datetime(2022,8,number)
print(now.strftime("%A"))
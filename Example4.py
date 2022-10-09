from ast import While

number = int(input("Введите число: "))
count = 1
if number > 0:
    while count <= number:
        multiple2 = count%2
        if multiple2 == 0:
            print(count)
        count += 1
else:
    print("ERROR")
    
   
    
number = int(input("Введите номер четверти координатной прямой: "))
match number:
        case 1:
                print("x>0;y>0")
        case 2:
                print("x<0;y>0")
        case 3:
                print("x<0;y<0")
        case 4:
                print("x>0;y<0")
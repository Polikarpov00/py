#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
print("введите номер четверти")
num = int(input())

if  num > 4 or num < 1:
    print("ошибка")  
elif num == 1:
    print("x>0, y>0")
elif num == 2:
    print("x<0, y>0")  
elif num == 3:
    print("x<0, y<0")  
elif num == 4:
    print("x>0, y<0")    
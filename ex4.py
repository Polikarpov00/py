#Показать первую цифру дробной части числа
a = 1.634

num = a % 1
num = num *10 
num = round(num)
print(num)
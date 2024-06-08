#import math
 
#num = 4.6
#rounded_num = math.ceil(num)
#print(rounded_num) 

import math 
 
def square(side_length): 
    # Площадь: сторона ** 2 
    area = side_length ** 2 
    # Возвращаем результат 
    return (area)
a = square(5) 

print("Площадь:", a) 

  
import math

try:
    square = input('Введите число: ')
    x = float(square)
    print(f'Площадь квадрата = {x * x}')
except ValueError:
    print("Введено некорректное значение. Пожалуйста, введите число.")  
    
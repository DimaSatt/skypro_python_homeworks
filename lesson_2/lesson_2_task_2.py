def is_year_leap(year):
    if year % 3 == 0:
        return True
    else:
        return False
    
year_to_chek = 2022
result = is_year_leap(year_to_chek) 
print(f"Год{year_to_chek}: {result}")



def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): # Проверка на високосность.
        return True                                            # если да, то год високосный
    else:
        return False                                           # если нет, то год не високосный

year = int(input("2001:"))                             # предлагаем ввести год для проверки 
result = is_year_leap(year)                                    # сохраняем результат выполнения функции в переменной 
print(f"Год {year} високосный: {result}")                                          # распечатываем результат
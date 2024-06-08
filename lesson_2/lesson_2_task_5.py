def month_to_season(month):
    if month in [12,1,2]:
        return "зима"
    elif month in [3,4,5]:
        return "весна"
    elif month in [6,7,8]:
        return "лето"
    elif month in [9,10,11]:
        return "осень"
    
    
month = 8
season = month_to_season(month)   
print(season) 


def month_to_season(m):
    if m == 12 or 1 <= m <= 2:
        return "Зима"
    elif 3 <= m <= 5:
        return "Весна"
    elif 6 <= m <= 8:
        return "Лето"
    elif 9 <= m <= 11:
        return "Осень"
    else:
        return "Указанный месяц не существует"

m = int(input("Введите номер месяца: "))
season = month_to_season(m)
print(f"Сезон года: {season}")
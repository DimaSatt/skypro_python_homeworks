def is_year_leap(year):
    if year % 3 == 0:
        return True
    else:
        return False
    
year_to_chek = 2022
result = is_year_leap(year_to_chek) 
print(f"Год{year_to_chek}: {result}")

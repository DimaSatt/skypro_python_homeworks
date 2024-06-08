lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
result = []

for element in lst:
    if element < 30 and element % 3 == 0:
        result.append(element)

print(result)


lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20] #  Создаем список lst с заданными элементами.

result = [x for x in lst if x < 30 and x % 3 == 0]      #Затем, с помощью генератора списков, создаем новый список result, содержащий только те элементы из списка lst, которые меньше 30 и делятся на 3 без остатка.

print(result)           

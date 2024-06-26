
def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i) 

n = 15 #Пример: число 15
fizz_buzz(n)     


def fizz_buzz(n):                             #Для решения данной задачи нам нужно перебирать числа от 1 до n 
                                              #и проверять каждое из них на делимость на 3 и/или 5. Если число делится на 3, печатаем "Fizz", 
                                              # если на 5 – "Buzz", а если на оба – "FizzBuzz".
    for i in range(1, n+1):                   #Здесь мы использовали цикл for для перебора чисел от 1 до n (включительно). 
        if i % 3 == 0 and i % 5 == 0:         #Затем мы проверяем каждое число на делимость на 3 и/или 5 с помощью оператора % (возвращает остаток от деления).
            print("FizzBuzz")                 #Если остаток от деления на 3 и на 5 равен 0, то число делится и на 3, и на 5, поэтому мы печатаем "FizzBuzz". 
        elif i % 3 == 0:                      #
            print("Fizz")                     #Если остаток от деления на 3 равен 0, то число делится на 3, и мы печатаем "Fizz". 
        elif i % 5 == 0:
            print("Buzz")                     # Если остаток от деления на 5 равен 0, то число делится на 5, и мы печатаем "Buzz". 
        else:
            print(i)                          # Если ни одно из условий не выполняется, мы просто печатаем число.
            
fizz_buzz(17)

    



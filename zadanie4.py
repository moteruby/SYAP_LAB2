#Задание4
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1/num2
    print(result)
except ValueError:
    print("Введено не число")
except ZeroDivisionError:
    print("Деление на ноль")
finally:
    print("Программа завершена")
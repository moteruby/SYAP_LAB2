#Вариант 9
#Задание 1
def nod(a, b):
    while b != 0:
        a,b = b,a %b
    return a
print(str(nod(56,908)))
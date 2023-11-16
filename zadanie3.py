#Задание3
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
min_index = array.index(min(array))
for i in range(len(array)):
    if min_index in array[i]:
        row = i
        col = array[i].index(min_index)
print("Номер строки" + row)
print("Номер столбца" + col)
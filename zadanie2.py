#Задание 2
def analyze_input(arg):
    if type(arg) == dict:
        smallest_keys = sorted(arg, key = arg.get[:3])
        return smallest_keys
    elif type(arg) == list:
        arg = [x for x in arg if x != 0]
        positive_nums = [x for x in arg if x > 0]
        if len(positive_nums) >= 2:
            product = positive_nums[0] * positive_nums[1]
            return product
        else:
            return "Недостаточно положительных элементов"
    elif type(arg) == int:
        num_digits = len(str(arg))
        return num_digits
    elif type(arg) == str:
        char_dict = {}
        for char in arg:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
            return char_dict
    else:
        return "Неподдерживаемый тип аргумента"

arg = {1:2, 3:4, 5:6, 7:8, 9:10}
print(analyze_input(arg))

arg = [1, 2, 3, 0 , -2, -3]
print(analyze_input(arg))

arg = 123123
print(analyze_input(arg))

arg = "hello"
print(analyze_input(arg))
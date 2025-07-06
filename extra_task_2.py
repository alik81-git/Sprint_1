def digit_root(num):
    while num >= 10:
        sum_of_digits = 0
        for digit in str(num):
            sum_of_digits += int(digit)
        num = sum_of_digits
    return num    


num = 1122335
num_root = digit_root(num)
print(num_root)
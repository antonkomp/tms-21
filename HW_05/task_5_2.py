number = 2345
number_list = list(str(number))
sum_number = 0
mult_number = 1
for i in number_list:
    sum_number += int(i)
    mult_number *= int(i)
print(sum_number)
print(mult_number)

for iter_1 in range(200, 301):
    friendly_number_1 = 0
    friendly_number_2 = 0
    for iter_2 in range(1, iter_1):
        if iter_1 % iter_2 == 0:
            friendly_number_1 += iter_2
    for iter_3 in range(1, friendly_number_1):
        if friendly_number_1 % iter_3 == 0:
            friendly_number_2 += iter_3
    if iter_1 == friendly_number_2 and iter_1 != friendly_number_1 and iter_1 == min(iter_1, friendly_number_1):
        print(friendly_number_2, friendly_number_1)

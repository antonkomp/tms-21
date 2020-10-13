def solution_for(start_dict):
    for key in list(start_dict):
        new_dict = {f'{key}{len(key)}': start_dict[key]}
        start_dict.update(new_dict)
        del start_dict[key]
    print(start_dict)


def solution_while(start_dict):
    dict_keys = list(start_dict)
    dict_values = list(start_dict.values())
    counter = 0
    while counter < len(dict_keys):
        new_dict = {f'{dict_keys[counter]}{len(dict_keys[counter])}': dict_values[counter]}
        start_dict.update(new_dict)
        del start_dict[dict_keys[counter]]
        counter += 1
    print(start_dict)


start_dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
solution_for(start_dict_1)
start_dict_2 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
solution_while(start_dict_2)

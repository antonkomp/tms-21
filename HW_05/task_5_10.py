from datetime import datetime, timedelta

train_1 = {'train_№': 321, 'departure_station': 'Moscow', 'departure_time': datetime(2020, 10, 13, 6, 40),
           'arrival_station': 'Minsk', 'arrival_time': datetime(2020, 10, 13, 16, 10)}
train_2 = {'train_№': 456, 'departure_station': 'Grodno', 'departure_time': datetime(2020, 10, 12, 13, 20),
           'arrival_station': 'Minsk', 'arrival_time': datetime(2020, 10, 12, 18, 00)}
train_3 = {'train_№': 876, 'departure_station': 'Warsaw', 'departure_time': datetime(2020, 10, 12, 20, 00),
           'arrival_station': 'Minsk', 'arrival_time': datetime(2020, 10, 13, 3, 50)}
list_train = [train_1, train_2, train_3]
for dict_i in list_train:
    travel_time = dict_i['arrival_time'] - dict_i['departure_time']
    interval = timedelta(hours=7, minutes=20)
    if travel_time > interval:
        for key in dict_i:
            print(key, ':', dict_i[key])
        print('travel time :', travel_time)
        print()

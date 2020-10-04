start_list = [i for i in range(10)]


def solution_for():
    counter_with_for = 0
    for iterat in start_list:
        if iterat % 2 == 0:
            counter_with_for += 1
    print(counter_with_for)


def solution_while():
    counter_with_while = 0
    iterat = 0
    while iterat < len(start_list):
        if start_list[iterat] % 2 == 0:
            counter_with_while += 1
        iterat += 1
    print(counter_with_while)


solution_for()
solution_while()

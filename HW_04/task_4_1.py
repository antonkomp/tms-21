start_list = [i for i in range(10)]


def solution_for():
    new_list_1 = [i * -2 for i in start_list]
    print(new_list_1)


def solution_while():
    iterat = 0
    new_list_2 = []
    while iterat < len(start_list):
        new_list_2.append(start_list[iterat] * -2)
        iterat += 1
    print(new_list_2)


solution_for()
solution_while()

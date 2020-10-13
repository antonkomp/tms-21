start_list = [i for i in range(10)]


def solution_for():
    new_list = []
    for step in range(len(start_list)):
        if step != 0:
            new_list.append(start_list[step])
    new_list.append(start_list[0])
    print(new_list)


def solution_while():
    new_list = []
    counter = 0
    while counter < len(start_list):
        if counter != 0:
            new_list.append(start_list[counter])
        counter += 1
    new_list.append(start_list[0])
    print(new_list)


solution_for()
solution_while()

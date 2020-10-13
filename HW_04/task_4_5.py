def solution_for(first=1, second=1):
    for _ in range(14):
        first, second = second, second + first
        fibonacci_list_for.append(first)
    print(fibonacci_list_for)


def solution_while(first=1, second=1):
    counter = 0
    while counter < 14:
        first, second = second, second + first
        fibonacci_list_while.append(first)
        counter += 1
    print(fibonacci_list_while)


fibonacci_list_for = [1]
fibonacci_list_while = [1]
solution_for()
solution_while()

string = input()
center_letter = int(len(string) / 2)
print(string[center_letter])

if string[0] == string[center_letter]:
    new_string = string[1:-1]
    print(new_string)

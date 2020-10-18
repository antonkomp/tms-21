start_string = "Python is an interpreted high-level and general-purpose programming language"
list_string = start_string.split(' ')
for i, item in enumerate(list_string):
    list_string[i] = item[::-1]
end_string = ' '.join(list_string)
print(end_string)

with open('test_file.txt', 'r') as file:
    print(file)
    for line in file:
        print(line)

with open('test_file.txt', 'r', encoding='utf8') as file:
    print(file)
    for line in file:
        print(line)
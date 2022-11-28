def draw(numbers_of_stars):
    for i in range(numbers_of_stars):
        line = ''
        for j in range(i, numbers_of_stars):
            line = f'{line}*'
        print(line)


draw(10)



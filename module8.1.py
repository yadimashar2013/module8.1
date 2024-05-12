def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        print(add_everything_up(str(123.456), 'строка'))
        print(add_everything_up('яблоко', str(4215)))
        print(round(add_everything_up(123.456, 7), 3))


add_everything_up(1, 'c')


def add_everything_up(a, b):
    try:

        result = a + b
        return result
    except TypeError:

        return str(a) + str(b)


# Пример использования функции:
if __name__ == "__main__":
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))

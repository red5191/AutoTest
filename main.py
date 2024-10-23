print('1. Какое из двух чисел больше?')


def input_max_of_two():
    try:
        global a, b
        a = float(input('Введите первое число '))
        b = float(input('Введите второе число '))
    except ValueError:
        print('Это не число, попробуй снова', '\n')
        input_max_of_two()
    else:
        return a, b


input_max_of_two()


def max_of_two(a, b):
    if a != b:
        return max(a, b)
    else:
        return 'Введенные числа равны!'


print(f'{max_of_two(a, b)}', '\n')


def empty():
    pass


def input_even_num():
    global n
    while True:
        try:
            n = int(input('3. Перечислим все четные числа до '))
        except ValueError:
            print('Это не число, попробуй снова', '\n')
        else:
            return n


input_even_num()


def even_num(n):
    for num in range(0, (int(n) + 1), 2):
        yield num


for x in even_num(n):
    print(x)


# 4
def test_max_of_two():
    assert max_of_two(64, 95) == 95, "4. Ошибка: другое число больше"
    assert max_of_two(-48, 3) == 3, "4. Ошибка: другое число больше"
    assert max_of_two(-56, -5) == -5, "4. Ошибка: другое число больше"
    assert max_of_two(5, 5) == 'Введенные числа равны!', '4. Введенные числа равны!'


test_max_of_two()
print('4. Все тесты пройдены!')

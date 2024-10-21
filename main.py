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


print(f'2.{empty()}', '\n')


def input_even_num():
    try:
        global n
        n = float(input('3. Перечислим все четные числа до '))
    except ValueError:
        print('Это не число, попробуй снова', '\n')
        input_even_num()
    else:
        return n


input_even_num()


def even_num(n):
    if n >= 0:
        for num in range(int(n / 2 + 1)):
            yield num * 2
    elif n < 0:
        for num in range(abs(int(- n / 2 + 1))):
            yield num * (- 2)


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

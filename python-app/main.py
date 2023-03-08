import calendar


def my_foo():
    pass


if __name__ == '__main__':
    print("Добро пожаловать в суперклалендарь\n")

    year = int(input('Пожалуйста введите год: '))
    month = int(input('Введите номер любого месяца: '))

    print(calendar.month(year, month))

    print('Всего хорошего!')

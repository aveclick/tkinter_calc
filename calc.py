from tkinter import *
"""
Добавляем цифру в строку ввода; 
С помощью метода get получаем данные в строке ввода и прибавляем к ним в виде строки нашу цифру;
С помощью метода delete очищаем строку ввода от самого начала(нулевого индекса) до конца(переменная END);
Метод insert отвечает за вставку.
"""


def add_num(number):
    value = entry_calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    entry_calc.insert(0, value + number)
    entry_calc['state'] = DISABLED


# Знаки операций заменяются друг другом.
def add_operation(operation):
    value = entry_calc.get()

    if value[-1] in '-+÷×.':
        # При помощи среза сохраняем все, кроме последней операции.
        value = value[:-1]

    # Если уже есть операция, то вычисляем и затем выводим новое значение.
    elif '+' in value or '-' in value or '÷' in value or '×' in value:
        calculate()
        value = entry_calc.get()

    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    entry_calc.insert(0, value + operation)
    entry_calc['state'] = DISABLED


# Функция eval-разбирает и выполняет указанное выражение(если оно представлено в форме строки).
def calculate():
    value = entry_calc.get()
    k = 0
    for i in value:
        if i == '÷':
            value = value[0:k] + '/' + value[k + 1:]
            break
        k += 1

    k = 0
    for i in value:
        if i == '×':
            value = value[0:k] + '*' + value[k + 1:]
            break
        k += 1

    # Выполняем действие числа с числом, если последний символ в строке-знак операции.
    if value[-1] in '+-/*':
        value = value + value[:-1]

    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    try:
        entry_calc.insert(0, eval(value))
        entry_calc['state'] = DISABLED
    except (NameError, SyntaxError, ZeroDivisionError):
        clear()
        entry_calc['state'] = DISABLED


def comma_to_point():
    value = entry_calc.get()
    if value[-1] in '-+÷×':
        entry_calc['state'] = NORMAL
        entry_calc.delete(0, END)
        entry_calc.insert(0, value + '0' + '.')
        entry_calc['state'] = DISABLED
    elif '+' in value or '-' in value or '÷' in value or '×' in value:
        k = 0
        for i in value:
            if i == '+' or i == '-' or i == '÷' or i == '×':
                break
            k += 1

        k = 0
        for i in value[k:]:
            if i == '.':
                k += 1

        if k < 1:
            value = value + '.'
            entry_calc['state'] = NORMAL
            entry_calc.delete(0, END)
            entry_calc.insert(0, value)
            entry_calc['state'] = DISABLED

    else:
        k = 0

        for i in value:
            if i == '.':
                k += 1
        if k < 1:
            value = value + '.'
            entry_calc['state'] = NORMAL
            entry_calc.delete(0, END)
            entry_calc.insert(0, value)
            entry_calc['state'] = DISABLED


def calculate_per():
    value = entry_calc.get()
    if value[0] == "0" and len(value) == 1:
        clear()
    elif '+' in value or '-' in value or '÷' in value or '×' in value:
        calculate()
        value = entry_calc.get()
        entry_calc['state'] = NORMAL
        entry_calc.delete(0, END)
        entry_calc.insert(0, float(value) / 100)
        entry_calc['state'] = DISABLED
    else:
        entry_calc['state'] = NORMAL
        entry_calc.delete(0, END)
        entry_calc.insert(0, float(value) / 100)
        entry_calc['state'] = DISABLED


def plus_to_minus():
    value = entry_calc.get()
    if value[0] == "0" and len(value) == 1:
        clear()

    elif '+' in value or '-' in value or '÷' in value or '×' in value:
        calculate()
        value = entry_calc.get()
        entry_calc['state'] = NORMAL
        k = 0
        for i in value:
            if i == '.':
                k += 1
        if k > 0:
            entry_calc.delete(0, END)
            entry_calc.insert(0, float(value) / (-1))
        else:
            entry_calc.delete(0, END)
            entry_calc.insert(0, int(value) * (-1))
        entry_calc['state'] = DISABLED
    else:
        entry_calc['state'] = NORMAL
        k = 0
        for i in value:
            if i == '.':
                k += 1
        if k > 0:
            entry_calc.delete(0, END)
            entry_calc.insert(0, float(value) / (-1))
        else:
            entry_calc.delete(0, END)
            entry_calc.insert(0, int(value) * (-1))
        entry_calc['state'] = DISABLED


def del_symbol():
    value = entry_calc.get()
    if len(value) > 1:
        entry_calc['state'] = NORMAL
        entry_calc.delete(0, END)
        entry_calc.insert(0, value[:-1])
        entry_calc['state'] = DISABLED
    elif len(value) == 1 and value != '0':
        clear()


def clear():
    entry_calc['state'] = NORMAL
    entry_calc.delete(0, END)
    entry_calc.insert(0, '0')
    entry_calc['state'] = DISABLED


# Функция для создания кнопок, в качестве параметра передаем переменную number(цифру).

# Функция lambda реализует возможность многократных обратных вызывов.


def make_button(number):
    return Button(text=number, font=('Franklin Gothic Medium', 15), command=lambda: add_num(number))


# Добавляет операции, с помощью параметра fg меняем цвет.
def make_operation(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='thistle2',
                  command=lambda: add_operation(operation))


def make_calc(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='LightCyan2',
                  command=calculate)


def make_clear(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='LightCyan2',
                  command=clear)


def make_percent(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='thistle2',
                  command=calculate_per)


def make_minus(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='thistle2',
                  command=plus_to_minus)


def make_point(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='thistle2',
                  command=comma_to_point)


def make_del(operation):
    return Button(text=operation, font=('Franklin Gothic Medium', 18), fg='blue', bg='LightCyan2',
                  command=del_symbol)


# Метод .isdigit проверяет, цифра или нет.
# Функция для обработки нажатий на клавиши.
def press_key(event):
    if event.char.isdigit():
        add_num(event.char)
    elif event.char in '+-*/.':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


calc = Tk()

# Размер окна.
calc.geometry('240x339')

calc.resizable(width=False, height=False)

# Цвет фона окна.
calc['bg'] = '#CCCCFF'

# Название окна.
calc.title('Калькулятор')

# Обработка событий.

calc.bind("<Key>", press_key)

# Поле ввода, свойство justify отвечает за то, с какой стороны будет появляться текст в строке ввода.

entry_calc = Entry(calc, justify=RIGHT, font=('Franklin Gothic Medium', 18), width=15)

# Значение по умолчанию-0.
entry_calc.insert(0, '0')
entry_calc['state'] = DISABLED

"""
Задаем расположение поля ввода с помощью метода grid, объединяем колонки с помощью атрибута columnspan, 
растягиваем поле с помощью атрибута stick от west до east(от левой стороны до правой).
"""

entry_calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5, pady=3)

# Задаем расстояние между кнопками с помощью атрибутов padx и pady.

make_button('1').grid(row=4, column=0, stick='wens', padx=3, pady=3)
make_button('2').grid(row=4, column=1, stick='wens', padx=3, pady=3)
make_button('3').grid(row=4, column=2, stick='wens', padx=3, pady=3)
make_button('4').grid(row=3, column=0, stick='wens', padx=3, pady=3)
make_button('5').grid(row=3, column=1, stick='wens', padx=3, pady=3)
make_button('6').grid(row=3, column=2, stick='wens', padx=3, pady=3)
make_button('7').grid(row=2, column=0, stick='wens', padx=3, pady=3)
make_button('8').grid(row=2, column=1, stick='wens', padx=3, pady=3)
make_button('9').grid(row=2, column=2, stick='wens', padx=3, pady=3)
make_button('0').grid(row=5, column=1, stick='wens', padx=3, pady=3)

# Создаем операции.
make_operation('+').grid(row=4, column=3, stick='wens', padx=3, pady=3)
make_operation('-').grid(row=3, column=3, stick='wens', padx=3, pady=3)
make_operation('÷').grid(row=1, column=3, stick='wens', padx=3, pady=3)
make_operation('×').grid(row=2, column=3, stick='wens', padx=3, pady=3)

make_point(',').grid(row=5, column=2, stick='wens', padx=3, pady=3)
make_percent('%').grid(row=1, column=0, stick='wens', padx=3, pady=3)
make_minus('+/-').grid(row=5, column=0, stick='wens', padx=3, pady=3)
make_calc('=').grid(row=5, column=3, stick='wens', padx=3, pady=3)
make_clear('AC').grid(row=1, column=2, stick='wens', padx=3, pady=3)
make_del('<-').grid(row=1, column=1, stick='wens', padx=3, pady=3)

# С помощью метода grid_column(row)configure задаем минимальный размер колонок(column) и строк(row).
calc.grid_columnconfigure(0, minsize=60)
calc.grid_columnconfigure(1, minsize=60)
calc.grid_columnconfigure(2, minsize=60)
calc.grid_columnconfigure(3, minsize=60)

calc.grid_rowconfigure(1, minsize=60)
calc.grid_rowconfigure(2, minsize=60)
calc.grid_rowconfigure(3, minsize=60)
calc.grid_rowconfigure(4, minsize=60)

# Запуск приложения.
calc.mainloop()

import tkinter as tk
from PIL import Image, ImageTk
from decimal import *


def clear():
    equation_label['text'] = '0'


def plus_minus():
    if len(equation_label['text']) <= 20 and equation_label['text'][-1].isdigit():
        split = equation_label['text'].split(' ')
        if len(split) >= 2 and (split[-2] == '+' or split[-2] == '−'):
            if split[-2] == '+':
                split[-2] = '−'
            elif split[-2] == '−':
                split[-2] = '+'
        elif equation_label['text'][-1].isdigit():
            try:
                split[-1] = (str(int(split[-1]) * (-1)))
            except ValueError:
                split[-1] = (str(float(split[-1]) * (-1)))
        equation_label['text'] = split


def percent():
    split = equation_label['text'].split(' ')
    if len(equation_label['text']) <= 18 and split[-1].isdigit():
        try:
            split[-1] = str(int(split[-1]) / 100)
        except ValueError:
            split[-1] = str(float(split[-1]) / 100)
            equation_label['text'] = split


def operator(op):
    if len(equation_label['text']) <= 20:
        split = equation_label['text'].split(' ')
        if len(split) >= 2:
            if split[-1] == '':
                del split[-1]
            if split[-1] == '+' or split[-1] == '−' or split[-1] == '×' or split[-1] == '÷':
                del split[-1]
                split.append(op,)
                equation_label['text'] = split
        if equation_label['text'][-1].isdigit():
            equation_label['text'] += ' ' + op + ' '
        elif equation_label['text'][-1] == '.':
            equation_label['text'] = equation_label['text'][0:-1]
            equation_label['text'] += ' ' + op + ' '


def num_input(num):
    if equation_label['text'] == '0':
        equation_label['text'] = num
    elif len(equation_label['text']) <= 20:
        equation_label['text'] += num


def decimal():
    if len(equation_label['text']) <= 18:
        split = equation_label['text'].split(' ')
        if '.' not in split[-1] and split[-1].isdigit():
            equation_label['text'] += '.'
        else:
            equation_label['text'] += '0.'


# Incomplete for addition and subtraction
# Fix zero division error (0 works... 0.0 gives error)
# Fix inability to multiply floats (as second number)
# Long answers from division
def solve():
    split = equation_label['text'].split(' ')
    solved = ''
    while not split[-1].isdigit() and not (str(int(split[-1]) * -1)).isdigit():
        del split[-1]
    while '×' in split and '÷' in split:
        if split.index('×') < split.index('÷'):
            try:
                result = str(int(split[split.index('×') - 1]) * int(split[split.index('×') + 1]))
            except ValueError:
                result = str(Decimal(split[split.index('×') - 1]) * Decimal(split[split.index('×') + 1]))
            solved = result
            split[split.index('×')] = result
            del split[split.index(result) - 1]
            del split[split.index(result) + 1]
        else:
            if split[split.index('÷') + 1] == '0' or split[split.index('÷') + 1] == '0.0':
                result = '0'
                solved = result
                split[split.index('÷')] = result
                del split[split.index(result) - 1]
                del split[split.index(result) + 1]
            else:
                try:
                    result = str(int(split[split.index('÷') - 1]) / int(split[split.index('÷') + 1]))
                    solved = result
                    split[split.index('÷')] = result
                except ValueError:
                    result = str(Decimal(split[split.index('÷') - 1]) / Decimal(split[split.index('÷') + 1]))
                    solved = result
                    split[split.index('÷')] = result
                del split[split.index(result) - 1]
                del split[split.index(result) + 1]
    while '×' in split:
        try:
            result = str(int(split[split.index('×') - 1]) * int(split[split.index('×') + 1]))
        except ValueError:
            result = str(Decimal(split[split.index('×') - 1]) * Decimal(split[split.index('×') + 1]))
        solved = result
        split[split.index('×')] = result
        del split[split.index(result) - 1]
        del split[split.index(result) + 1]
    while '÷' in split:
        if split[split.index('÷') + 1] == '0' or split[split.index('÷') + 1] == '0.0':
            result = '0'
            solved = result
            split[split.index('÷')] = result
            del split[split.index(result) - 1]
            del split[split.index(result) + 1]
        else:
            if '.' in split[split.index('÷') - 1] or split[split.index('÷') + 1]:
                result = str(Decimal(split[split.index('÷') - 1]) / Decimal(split[split.index('÷') + 1]))
            else:
                try:
                    result = str(int(int(split[split.index('÷') - 1]) / int(split[split.index('÷') + 1])))
                except ValueError:
                    result = str(Decimal(split[split.index('÷') - 1]) / Decimal(split[split.index('÷') + 1]))
            solved = result
            split[split.index('÷')] = result
            del split[split.index(result) - 1]
            del split[split.index(result) + 1]

    # while '+' in split and '−' in split:
    #     if split.index('+') < split.index('−'):
    #         solved += str(int(split[split.index('+')-1]) * int(split[split.index('+')+1]))
    #     else:
    #         pass

    equation_label['text'] = solved


if __name__ == '__main__':
    # Window Configuration
    main_window = tk.Tk()
    main_window.title("Calculator")
    main_window['bg'] = 'black'
    main_window.resizable(width=0, height=0)

    ico = Image.open('pb.png')
    photo = ImageTk.PhotoImage(ico)
    main_window.wm_iconphoto(False, photo)

    # Equation Label
    equation_label = tk.Label(text='0', bg='black', fg='white', font=20, pady=25, padx=10)
    equation_label.grid(row=0, column=0, rowspan=2, columnspan=4, sticky='se')

    # Buttons - Row 1
    button_ac = tk.Button(text="AC", bg='gray', fg='white', font=20, width=5, command=lambda: clear())
    button_ac.grid(row=2, column=0)
    button_plusminus = tk.Button(text="+/−", bg='gray', fg='white', font=20, width=5, command=lambda: plus_minus())
    button_plusminus.grid(row=2, column=1)
    button_percent = tk.Button(text="%", bg='gray', fg='white', font=20, width=5, command=lambda: percent())
    button_percent.grid(row=2, column=2)
    button_divide = tk.Button(text="÷", bg='gray', fg='white', font=20, width=5, command=lambda: operator("÷"))
    button_divide.grid(row=2, column=3)

    # Buttons - Row 2
    button_7 = tk.Button(text="7", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("7"))
    button_7.grid(row=3, column=0)
    button_8 = tk.Button(text="8", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("8"))
    button_8.grid(row=3, column=1)
    button_9 = tk.Button(text="9", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("9"))
    button_9.grid(row=3, column=2)
    button_multiply = tk.Button(text="×", bg='gray', fg='white', font=20, width=5, command=lambda: operator("×"))
    button_multiply.grid(row=3, column=3)

    # Buttons - Row 3
    button_4 = tk.Button(text="4", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("4"))
    button_4.grid(row=4, column=0)
    button_5 = tk.Button(text="5", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("5"))
    button_5.grid(row=4, column=1)
    button_6 = tk.Button(text="6", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("6"))
    button_6.grid(row=4, column=2)
    button_plus = tk.Button(text="+", bg='gray', fg='white', font=20, width=5, command=lambda: operator("+"))
    button_plus.grid(row=4, column=3)

    # Buttons - Row 4
    button_1 = tk.Button(text="1", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("1"))
    button_1.grid(row=5, column=0)
    button_2 = tk.Button(text="2", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("2"))
    button_2.grid(row=5, column=1)
    button_3 = tk.Button(text="3", bg='lightgray', fg='black', font=20, width=5, command=lambda: num_input("3"))
    button_3.grid(row=5, column=2)
    button_minus = tk.Button(text="−", bg='gray', fg='white', font=20, width=5, command=lambda: operator("−"))
    button_minus.grid(row=5, column=3)

    # Buttons - Row 5
    button_0 = tk.Button(text="0", bg='lightgray', fg='black', font=20, width=10, padx=6, command=lambda: num_input("0"))
    button_0.grid(row=6, column=0, columnspan=2)
    button_decimal = tk.Button(text=".", bg='lightgray', fg='black', font=20, width=5, command=lambda: decimal())
    button_decimal.grid(row=6, column=2)
    button_equals = tk.Button(text="=", bg='gray', fg='white', font=20, width=5, command=lambda: solve())
    button_equals.grid(row=6, column=3)

    main_window.mainloop()

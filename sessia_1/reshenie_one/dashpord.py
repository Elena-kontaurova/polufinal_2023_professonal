''' окно дашборд'''
import tkinter as tk
# from random import randint

a = 10


def dablat(tak):
    ''' главное окно'''
    global text_o
    one = tk.Label(tak, width=40, height=18,
                   borderwidth=1, background='white',
                   relief='solid')
    one.place(x=0, y=0)
    text_o = tk.Label(one, text=f'{a}', font=('', 60, 'bold'),
                      background='white')
    text_o.place(x=90, y=80)
    plus_s = tk.Label(one, text='+', font=('', 20, 'bold'),
                      background='white')
    plus_s.place(x=240, y=120)
    minus = tk.Label(one, text='-', font=('', 20, 'bold'),
                     background='white')
    minus.place(x=20, y=120)
    plus_s.bind('<Button-1>', lambda event: plus())
    minus.bind('<Button-1>', lambda event: mnus())
    text_govno = tk.Label(one, text='Задач выполнено за сегодня',
                          font=('', 15), background='white')
    text_govno.place(x=7, y=190)
    one_nu = tk.Label(tak, width=40, height=18,
                      borderwidth=1, background='white',
                      relief='solid')
    one_nu.place(x=0, y=320)
    two = tk.Label(tak, width=40, height=18,
                   borderwidth=1, background='white',
                   relief='solid')
    tt = tk.Label(two, text='ТОП 5 сотрудников по закртым задачам',
                  background='white')
    tt.place(x=30, y=10)
    jj = tk.Label(two, text='№', background='white')
    jj.place(x=10, y=40)
    two.place(x=360, y=0)
    three = tk.Label(tak, width=40, height=18,
                     borderwidth=1, background='white',
                     relief='solid')
    three.place(x=725, y=0)
    nn = tk.Label(tak, width=92, height=18,
                  borderwidth=1, background='white',
                  relief='solid')
    nn.place(x=360, y=320)


def plus():
    ''' d'''
    global a
    a = a + 1
    text_o.config(text=f'{a}')


def mnus():
    ''' k'''
    global a
    a = a - 1
    text_o.config(text=f'{a}')

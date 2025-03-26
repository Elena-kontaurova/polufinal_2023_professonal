''' окно дашборд'''
import tkinter as tk

a = 10


def dablat(tak):
    ''' главное окно'''
    global text_o, kol_one, kol_two, kol_three
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
    hahaha = tk.Label(one_nu, text='Экспорт данных', background='white')
    hahaha.place(x=10, y=10)
    yask = tk.Label(one_nu,
                    text='\u0332В\u0332с\u0332е\u0332'
                    ' \u0332з\u0332а\u0332д\u0332а\u0332ч\u0332и\u0332',
                    font=('', 12),
                    background='white')
    yask.place(x=10, y=30)
    sotr = tk.Label(one_nu,
                    text='\u0332В\u0332с\u0332е '
                    '\u0332с\u0332о\u0332т\u0332р\u0332у\u0332д'
                    '\u0332н\u0332и\u0332к\u0332и',
                    font=('', 12),
                    background='white')
    sotr.place(x=10, y=55)
    xax = tk.Label(one_nu, text='\u0332З\u0332а\u0332к\u0332'
                   'р\u0332ы\u0332т\u0332ы\u0332е\u0332 '
                   '\u0332з\u0332а\u0332д\u0332а\u0332ч\u0332и',
                   font=('', 12),
                   background='white')
    xax.place(x=10, y=80)
    two = tk.Label(tak, width=40, height=18,
                   borderwidth=1, background='white',
                   relief='solid')
    tt = tk.Label(two, text='ТОП 5 сотрудников по закртым задачам',
                  background='white')
    tt.place(x=20, y=10)
    jj = tk.Label(two, text='№', background='white')
    jj.place(x=10, y=40)
    stroks = tk.Label(two,
                      text='_________________________________________________',
                      background='white')
    stroks.place(x=10, y=55)
    stro = tk.Label(two,
                    text='_________________________________________________',
                    background='white')
    stro.place(x=10, y=95)
    strok = tk.Label(two,
                     text='_________________________________________________',
                     background='white')
    strok.place(x=10, y=135)
    palka_one = tk.Label(two,
                         text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|',
                         background='white')
    palka_one.place(x=30, y=40)
    abj = tk.Label(two, text='ФИО', background='white')
    abj.place(x=40, y=40)
    palka_two = tk.Label(two,
                         text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|',
                         background='white')
    palka_two.place(x=210, y=40)
    kol_vo = tk.Label(two, text='Кол-во', background='white')
    kol_vo.place(x=215, y=40)
    text_num_one = tk.Label(two, text='1', background='white')
    text_num_one.place(x=10, y=80)
    text_num_two = tk.Label(two, text='1', background='white')
    text_num_two.place(x=10, y=120)
    text_num_three = tk.Label(two, text='1', background='white')
    text_num_three.place(x=10, y=160)
    text_one = tk.Label(two, text='Петров Василий Иванович',
                        background='white')
    text_one.place(x=40, y=80)
    text_two = tk.Label(two, text='Петров Василий Иванович',
                        background='white')
    text_two.place(x=40, y=120)
    text_three = tk.Label(two, text='Петров Василий Иванович',
                          background='white')
    text_three.place(x=40, y=160)
    kol_one = tk.Label(two, text=a, background='white')
    kol_one.place(x=225, y=80)
    kol_two = tk.Label(two, text=a, background='white')
    kol_two.place(x=225, y=120)
    kol_three = tk.Label(two, text=a, background='white')
    kol_three.place(x=225, y=160)
    two.place(x=360, y=0)
    three = tk.Label(tak, width=40, height=18,
                     borderwidth=1, background='white',
                     relief='solid')
    uh = tk.Label(three, text='График задач по статусам',
                  background='white')
    uh.place(x=10, y=10)
    text_go = tk.Label(three, text='Место для графика',
                       font=('', 15), background='white')
    text_go.place(x=40, y=110)
    three.place(x=725, y=0)
    nn = tk.Label(tak, width=92, height=18,
                  borderwidth=1, background='white',
                  relief='solid')
    dia = tk.Label(nn, text='Тепловая диаграмма',
                   background='white')
    dia.place(x=10, y=10)
    text_gow = tk.Label(nn, text='Место для широкого графика',
                        font=('', 15), background='white')
    text_gow.place(x=200, y=110)
    nn.place(x=360, y=320)


def plus():
    ''' d'''
    global a
    a = a + 1
    text_o.config(text=f'{a}')
    kol_one.config(text=a)
    kol_two.config(text=a)
    kol_three.config(text=a)


def mnus():
    ''' k'''
    global a
    a = a - 1
    text_o.config(text=f'{a}')
    kol_one.config(text=a)
    kol_two.config(text=a)
    kol_three.config(text=a)

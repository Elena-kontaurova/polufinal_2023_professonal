''' kk'''
import tkinter as tk


def dablat(tak):
    ''' k'''
    one = tk.Label(tak, width=40, height=18,
                   borderwidth=1, background='white',
                   relief='solid')
    one.place(x=0, y=0)
    one_nu = tk.Label(tak, width=40, height=18,
                      borderwidth=1, background='white',
                      relief='solid')
    one_nu.place(x=0, y=320)
    two = tk.Label(tak, width=40, height=18,
                   borderwidth=1, background='white',
                   relief='solid')
    two.place(x=360, y=0)
    three = tk.Label(tak, width=40, height=18,
                     borderwidth=1, background='white',
                     relief='solid')
    three.place(x=725, y=0)
    nn = tk.Label(tak, width=92, height=18,
                  borderwidth=1, background='white',
                  relief='solid')
    nn.place(x=360, y=320)

''' k'''
import datetime
import tkinter as tk
from tkinter import PhotoImage
from connect_bd import TaskTask


def did():
    ''' jhj'''
    task = TaskTask.select()
    return task


def mimi(taaak):
    ''' j'''
    task = did()

    for tasks in task:
        frame_one = tk.Frame(taaak, background='white', width=850, height=40,
                             borderwidth=1,
                             relief='solid')
        frame_one.pack(pady=5, padx=5)

        haha = tk.Label(frame_one, text=f'{tasks.nubver}',
                        background='white', fg='black')
        haha.place(x=4, y=10)
        pipi = '#35db59'
        if tasks.vaib == 'Открыта':
            pipi = '#c60cc9'
        elif tasks.vaib == 'В работе':
            pipi = '#35b4db'
        vaib = tk.Label(frame_one, text=f'{tasks.vaib}',
                        background=pipi, fg='black')
        vaib.place(x=80, y=10)
        opinasin = tk.Label(frame_one, text=f'{tasks.opinasin}',
                            background='white', fg='black')
        opinasin.place(x=150, y=10)
        name = tk.Label(frame_one, text=f'{tasks.name}',
                        background='white', fg='#5d5e5e')
        name.place(x=600, y=10)
        fifi = '#5d5e5e'
        if tasks.dedline < datetime.datetime.now():
            fifi = '#de0922'
        dedline = tk.Label(frame_one, text=f'{tasks.dedline}',
                           bg='white', fg=fifi)
        dedline.place(x=700, y=10)

        ima = PhotoImage(file='app_next_icon.png')
        ima_z = ima.zoom(1)

        imaima = tk.Label(frame_one, image=ima_z)
        imaima.place(x=820, y=14)

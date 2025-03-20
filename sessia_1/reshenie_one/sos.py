''' k'''
import datetime
import tkinter as tk
from tkinter import PhotoImage
from connect_bd import TaskTask


def open_wiw(frames, room, frame_one, haha, opinasin):
    ''' j'''
    hhh = 450
    for frame in frames:
        frame.config(width=hhh)
    mat = tk.Label(room, width=80, height=43,
                   borderwidth=1, relief='solid', background='white')
    mat.pack()
    frame_one.config(background='#afb2ed')
    haha.config(background='#afb2ed')
    opinasin.config(background='#afb2ed')


def did():
    ''' jhj'''
    task = TaskTask.select()
    return task


def mimi(taaak, room):
    ''' j'''
    task = did()
    frames = []

    for tasks in task:
        frame_one = tk.Frame(taaak, background='white', width=850, height=40,
                             borderwidth=1,
                             relief='solid')
        frame_one.pack(pady=5, padx=5)
        frames.append(frame_one)

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

        imaima.bind('<Button-1>', lambda event,
                    f=frames, g=frame_one, d=haha, s=opinasin:
                    open_wiw(f, room, g, d, s))


# root = tk.Tk()
# root.geometry('900x500')

# ts = tk.Frame(root, width=800, height=500)
# ts.pack(anchor='w')

# mimi(ts, root)
# root.mainloop()

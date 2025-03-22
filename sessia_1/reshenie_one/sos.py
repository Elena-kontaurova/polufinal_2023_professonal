''' k'''
import datetime
import tkinter as tk
from tkinter import PhotoImage
from connect_bd import TaskTask, Task, TaskStatus


def open_wiw(frames, room, frame_one, haha, opinasin, task_id):
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
    mm = get_task_details(task_id)
    short_title = tk.Label(mat, text=f'{mm.short_title}', font=('', 12),
                           background='white', fg='#5d5e5e')
    short_title.place(x=25, y=15)
    description = tk.Label(mat, text=f'{mm.description}', font=('', 11),
                           background='white', fg='black')
    description.place(x=110, y=16)
    sosite = mm.status_id
    n = get_status(sosite)
    bibica = 'Открыта'
    zalupa = '#c60cc9'
    if n == 2:
        bibica = 'В работе'
        zalupa = '#51a5e0'
    elif n == 3:
        bibica = 'Закрыта'
        zalupa = '#35db59'
    status_id = tk.Label(mat, text=bibica, font=('', 11),
                         background=zalupa, fg='black')
    status_id.place(x=410, y=16)
    text_created_time = tk.Label(mat, text='Создание задачи:', font=('', 10),
                                 background='white', fg='black')
    text_created_time.place(x=25, y=45)
    created_time = tk.Label(mat, text=f'{mm.created_time}', font=('', 10),
                            background='white', fg='black')
    created_time.place(x=150, y=45)
    text_deadline = tk.Label(mat, text='Дедлайн:', font=('', 10),
                             background='white', fg='black')
    text_deadline.place(x=25, y=70)
    deadline = tk.Label(mat, text=f'{mm.deadline}', font=('', 10),
                        background='white', fg='black')
    deadline.place(x=100, y=70)
    text_full_title = tk.Label(mat, text='Предшествующая задача',
                               font=('', 10), background='white', fg='black')
    text_full_title.place(x=25, y=100)
    full_title = tk.Label(mat, text=f'{mm.full_title}', font=('', 11),
                          borderwidth=1, relief='solid',
                          background='white', fg='#5d5e5e',
                          width=40, height=2, anchor='w',
                          padx=10)
    full_title.place(x=25, y=130)
    text_start_actual_time = tk.Label(mat, background='white', fg='black',
                                      text='Фактическое начало выполнения:',
                                      font=('', 10))
    text_start_actual_time.place(x=25, y=175)
    start_actual_time = tk.Label(mat, background='white', fg='black',
                                 text=f'{mm.start_actual_time}',
                                 font=('', 10))
    start_actual_time.place(x=240, y=175)
    text_finish_actual_time = tk.Label(mat, background='white', fg='black',
                                       text='Фактическое завершение:',
                                       font=('', 10))
    text_finish_actual_time.place(x=25, y=200)
    finish_actual_time = tk.Label(mat, background='white', fg='black',
                                  text=f'{mm.finish_actual_time}',
                                  font=('', 10))
    finish_actual_time.place(x=190, y=200)
    opisanii = tk.Label(mat, text='Описание задачи',
                        borderwidth=1, relief='solid',
                        background='white', fg='black',
                        font=('', 10), width=50,
                        height=4, anchor='nw', padx=10, pady=10)
    opisanii.place(x=25, y=230)
    text_previous_task_id = tk.Label(mat, text='Исполнитель', font=('', 10),
                                     background='white', fg='black')
    text_previous_task_id.place(x=25, y=330)
    previous_task_id = tk.Label(mat, text=f'{mm.previous_task_id}',
                                font=('', 10), background='white', fg='black',
                                borderwidth=1, relief='solid',
                                width=22, height=1, padx=10, anchor='w',
                                pady=3)
    previous_task_id.place(x=25, y=355)
    prilog = tk.Label(mat, text='Приложения', font=('', 10),
                      background='white', fg='black')
    prilog.place(x=25, y=390)
    pripri = tk.Label(mat, text=f'{mm.icon}',
                      font=('', 10), background='white', fg='black',
                      borderwidth=1, relief='solid',
                      width=22, height=1, padx=10, anchor='w', pady=3)
    pripri.place(x=25, y=415)
    dob = tk.Label(mat, text='Добавить',
                   font=('', 10), background='white', fg='black',
                   borderwidth=1, relief='solid',
                   width=22, height=1, padx=10, anchor='w', pady=3)
    dob.place(x=25, y=445)
    nablid = tk.Label(mat, text='Наблюдатели', font=('', 10),
                      background='white', fg='black')
    nablid.place(x=25, y=485)
    skoks = tk.Label(mat, text='Петров Игорь',
                     font=('', 10), background='white', fg='black',
                     borderwidth=1, relief='solid',
                     width=22, height=1, padx=10, anchor='w', pady=3)
    skoks.place(x=25, y=510)
    dob_x = tk.Label(mat, text='Добавить',
                     font=('', 10), background='white', fg='black',
                     borderwidth=1, relief='solid',
                     width=22, height=1, padx=10, anchor='w', pady=3)
    dob_x.place(x=25, y=540)
    sox = tk.Label(mat, text='Сохранить',
                   font=('', 10), background='#021352', fg='white',
                   borderwidth=1, relief='solid',
                   width=22, height=2, anchor='center')
    sox.place(x=25, y=600)
    susu = tk.Label(mat, background='white', text='Удалить',
                    fg='#f00722',
                    width=22, height=2,
                    borderwidth=0, highlightthickness=2,
                    highlightbackground='#f00722',
                    highlightcolor='#f00722')
    susu.place(x=220, y=600)


def get_status(st):
    ''' j'''
    status = TaskStatus.get(TaskStatus.id == st)
    return status.id


def get_task_details(task_id):
    ''' u'''
    taskii = Task.get(Task.id == task_id)
    return taskii


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

        task_id = tasks.id
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
                    f=frames, g=frame_one, d=haha, s=opinasin, z=task_id:
                    open_wiw(f, room, g, d, s, z))

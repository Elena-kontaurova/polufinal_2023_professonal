''' левое меню'''
import tkinter as tk
from tkinter import PhotoImage


def open_new_window(_):
    ''' llk'''
    new_c = tk.Label(root, background='#424f7d', text='дашборд',
                     width=150, height=47)
    new_c.place(x=70, y=0)


def open_win(_):
    ''' llk'''
    new_c_c = tk.Label(root, width=150, height=47)
    new_c_c.place(x=70, y=0)
    name = tk.Label(new_c_c, text='Список задач', font=('', 12, 'bold'))
    name.pack(padx=20, pady=15)


def open_bll(_):
    ''' llk'''
    new_c_w = tk.Label(root, background='#424f7d', text='календарь',
                       width=150, height=47)
    new_c_w.place(x=70, y=0)


root = tk.Tk()
root.geometry('1137x712')
# root.resizable(False, False)
root.title('Меню')

main = tk.Frame(root, background='#021352', width=70, height=600)
main.pack(anchor='w')

main_icon = tk.Frame(main, background='#021352', width=125, height=100)
main_icon.pack(anchor='w')

main_icon_two = tk.Frame(main, background='#021352', width=125, height=100)
main_icon_two.pack(anchor='w')

main_icon_three = tk.Frame(main, background='#021352', width=125, height=100)
main_icon_three.pack(anchor='w')

main_icon_four = tk.Frame(main, background='#021352', width=125, height=100)
main_icon_four.pack(anchor='w')

app_icon = PhotoImage(file='app_icon.png')
app_icon = app_icon.subsample(11)
logo_lable = tk.Label(main_icon, image=app_icon, bg='#021352')
logo_lable.pack(anchor='n', padx=11, pady=13)

app_dashboard = PhotoImage(file='app_dasboard_icon.png')
app_dashboard = app_dashboard.zoom(1)
logo_dashboard = tk.Label(main_icon_two, image=app_dashboard, bg='#021352')
logo_dashboard.pack(anchor='w', padx=26, pady=7)

app_tasks = PhotoImage(file='app_tasks_icon.png')
app_tasks = app_tasks.zoom(1)
logo_tasks = tk.Label(main_icon_three, image=app_tasks, bg='#021352')
logo_tasks.pack(anchor='w', padx=26, pady=5)

app_cal = PhotoImage(file='app_cal_icon.png')
app_cal = app_cal.zoom(1)
logo_cal = tk.Label(main_icon_four, image=app_cal, bg='#021352')
logo_cal.pack(anchor='w', padx=26, pady=5)

cartinca = tk.Label(main, background='#021352', text='ПУ',
                    fg='white',
                    width=5, height=2,
                    borderwidth=0, highlightthickness=2,
                    highlightbackground='white',
                    highlightcolor='white')
cartinca.pack(pady=6)

pupu = tk.Label(main, background='white', text='БУ',
                fg='#021352',
                width=5, height=2)
pupu.pack(pady=6)

susu = tk.Label(main, background='#021352', text='ЛА',
                fg='white',
                width=5, height=2,
                borderwidth=0, highlightthickness=2,
                highlightbackground='white',
                highlightcolor='white')
susu.pack(pady=6)

hh = tk.Label(main, background='#021352', width=3, height=24)
hh.pack()

hhh = tk.Label(main, background='#021352', text='1.4.2345',
               width=5, height=3, fg='#91939c')
hhh.pack()

logo_dashboard.bind("<Button-1>", open_new_window)

logo_tasks.bind("<Button-1>", open_win)

logo_cal.bind("<Button-1>", open_bll)

root.mainloop()

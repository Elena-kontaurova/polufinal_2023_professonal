''' левое меню'''
import tkinter as tk
from tkinter import PhotoImage


def open_new_window(_):
    ''' llk'''
    new_window = tk.Toplevel()
    new_window.title("Новое Окно")
    new_window.geometry("200x100")
    tk.Label(new_window, text="Это новое окно").pack(pady=20)


root = tk.Tk()
root.geometry('100x700')
# root.resizable(False, False)
root.title('Меню')

main_icon = tk.Frame(root, background='#021352', width=125, height=100)
main_icon.pack(anchor='w')

main_icon_two = tk.Frame(root, background='#021352', width=125, height=100)
main_icon_two.pack(anchor='w')

main_icon_three = tk.Frame(root, background='#021352', width=125, height=100)
main_icon_three.pack(anchor='w')

main_icon_four = tk.Frame(root, background='#021352', width=125, height=100)
main_icon_four.pack(anchor='w')

# main = tk.Frame(root, background='#021352', width=100, height=600)
# main.pack(anchor='w')

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

# logo_lable.bind("<Button-1>", open_new_window)

root.mainloop()

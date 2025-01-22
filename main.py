import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        selected_task = started_listbox.curselection()
        if selected_task:
            started_listbox.delete(selected_task)
        else:
            selected_task = finished_listbox.curselection()
            if selected_task:
                finished_listbox.delete(selected_task)

def start_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        started_listbox.insert(tk.END, task_listbox.get(selected_task))
        task_listbox.delete(selected_task)

def finish_task():
    selected_task = started_listbox.curselection()
    if selected_task:
        finished_listbox.insert(tk.END, started_listbox.get(selected_task))
        started_listbox.delete(selected_task)


root = tk.Tk()
root.title('Task list')
root.configure(background='antiquewhite3')

text1 = tk.Label(root, text='Введите вашу задачу:', bg='antiquewhite3')
text1.grid(column=0, row=0, pady=5)

task_entry = tk.Entry(root, width=30, bg='antiquewhite4')
task_entry.grid(column=0, row=1, pady=10)

add_task_button = tk.Button(root, text='Добавить задачу', command=add_task, width=40)
add_task_button.grid(column=0, row=2, pady=5)

delete_button = tk.Button(root, text='Удалить задачу', command=delete_task, width=40)
delete_button.grid(column=1, row=0, pady=5)

start_task_button = tk.Button(root, text='Начать задачу', command=start_task, width=40)
start_task_button.grid(column=1, row=2, pady=5)

finish_task_button = tk.Button(root, text='Завершить задачу', command=finish_task, width=40)
finish_task_button.grid(column=2, row=2, pady=5)

text2 = tk.Label(root, text='Список задач:', bg='antiquewhite3')
text2.grid(column=0, row=3, pady=5)

task_listbox = tk.Listbox(root, height=10, width=50, bg='LightPink1')
task_listbox.grid(column=0, row=4, pady=10)

text3 = tk.Label(root, text='Начатые задачи:', bg='antiquewhite3')
text3.grid(column=1, row=3, pady=5)

started_listbox = tk.Listbox(root, height=10, width=50, bg='moccasin')
started_listbox.grid(column=1, row=4, pady=10)

text4 = tk.Label(root, text='Выполненные задачи:', bg='antiquewhite3')
text4.grid(column=2, row=3, pady=5)

finished_listbox = tk.Listbox(root, height=10, width=50, bg='aquamarine2')
finished_listbox.grid(column=2, row=4, pady=10)

text5 = tk.Label(root, text='Выберите задачу в списке зачач и\n нажмите на кнопку ниже, чтобы начать её.', bg='antiquewhite3')
text5.grid(column=1, row=1)

text6 = tk.Label(root, text='Выберите задачу в списке начатых зачач и\n нажмите на кнопку ниже, чтобы завершить её.', bg='antiquewhite3')
text6.grid(column=2, row=1)

text7 = tk.Label(root, text='- Удаляет выбранную задачу из любого списка.', bg='antiquewhite3')
text7.grid(column=2, row=0)

root.mainloop()
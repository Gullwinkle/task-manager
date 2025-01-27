import tkinter as tk
from tkinter import filedialog

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

def save_tasks():
    global file_name
    if file_name:
        task_list = task_listbox.get(0, tk.END)
        started_list = started_listbox.get(0, tk.END)
        finished_list = finished_listbox.get(0, tk.END)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(':!:'.join(task_list))
            file.write('\n')
            file.write(':!:'.join(started_list))
            file.write('\n')
            file.write(':!:'.join(finished_list))
    else:
        save_tasks_as()
def save_tasks_as():
    global file_name
    file_name = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
    root.title(f'Task list - {file_name.split("/")[-1]}')
    save_tasks()

def load_tasks():
    global file_name
    file_name = filedialog.askopenfilename()
    root.title(f'Task list - {file_name.split("/")[-1]}')
    task_listbox.delete(0, tk.END)
    started_listbox.delete(0, tk.END)
    finished_listbox.delete(0, tk.END)
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            tasks = file.read().split('\n')
            i_task = 0
            i_started = 0
            i_finished = 0
            for task in tasks[0].split(':!:'):
                task_listbox.insert(i_task, task)
                i_task += 1
            for task in tasks[1].split(':!:'):
                started_listbox.insert(i_started, task)
                i_started += 1
            for task in tasks[2].split(':!:'):
                finished_listbox.insert(i_finished, task)
                i_finished += 1
    except FileNotFoundError:
        pass

def new_file():
    global file_name
    file_name = None
    root.title('Task list')
    task_listbox.delete(0, tk.END)
    started_listbox.delete(0, tk.END)
    finished_listbox.delete(0, tk.END)

root = tk.Tk()
file_name = None
root.title('Task list')
root.configure(background='antiquewhite3')

main_menu = tk.Menu(root)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='Новый', command=new_file)
file_menu.add_command(label='Открыть', command=load_tasks)
file_menu.add_command(label='Сохранить', command=save_tasks)
file_menu.add_command(label='Сохранить как...', command=save_tasks_as)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=root.quit)
main_menu.add_cascade(label='Файл', menu=file_menu)
root.config(menu=main_menu)

text1 = tk.Label(root, text='Введите вашу задачу:', bg='antiquewhite3')
text1.grid(column=0, row=0, pady=5)

task_entry = tk.Entry(root, width=30, bg='antiquewhite4')
task_entry.bind('<Return>', lambda event: add_task())
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
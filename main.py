# Список задач

import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="chartreuse2")

# Добавление кнопки для сортировки списка:
def sort_tasks():
    tasks = task_listBox.get(0, tk.END)
    tasks = sorted(tasks)
    task_listBox.delete(0, tk.END)
    for task in tasks:
        task_listBox.insert(tk.END, task)

# Добавление кнопок для перемещения задач вверх и вниз:
def move_task_up():
    selected_task = task_listBox.curselection()
    if selected_task:
        index = selected_task[0]
        if index > 0:
            task = task_listBox.get(index)
            task_listBox.delete(index)
            task_listBox.insert(index-1, task)
            task_listBox.selection_clear(0, tk.END)
            task_listBox.select_set(index-1)

def move_task_down():
    selected_task = task_listBox.curselection()
    if selected_task:
        index = selected_task[0]
        if index < task_listBox.size() - 1:
            task = task_listBox.get(index)
            task_listBox.delete(index)
            task_listBox.insert(index+1, task)
            task_listBox.selection_clear(0, tk.END)
            task_listBox.select_set(index+1)


root = tk.Tk()
root.title("Task list")
# tk.Tk().title("Task list")
root.configure(background="HotPink")

text1 = tk.Label(root, text="Введите вашу задачу:")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="DeepPink1")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_button=tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(padx=5, pady=5)

text2 = tk.Label(root, text="Список задач:")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_listBox.pack(padx=5, pady=10)

# Кнопки для сортировки списка:
sort_button = tk.Button(root, text="Сортировать задачи", command=sort_tasks)
sort_button.pack(pady=5)

# Кнопки для перемещения задач вверх и вниз:
move_up_button = tk.Button(root, text="Переместить задачу вверх", command=move_task_up)
move_up_button.pack(pady=5)
move_down_button = tk.Button(root, text="Переместить задачу вниз", command=move_task_down)
move_down_button.pack(pady=5)


root.mainloop()

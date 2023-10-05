from tkinter import messagebox
import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json


# Concept: create a program that in which you can add to-dos,
#           estimate the time it will take and ask for suggestions when you have time
#           use TKinter!

# TODO: make window which takes name, time estimate and perhaps priority estimate

# TODO save data to a document (no database needed)

# TODO create suggest function to search for to-dos

# TODO create delete function to erase to-dos that are to-done

connection = sqlite3.connect("to-dos.db")
cursor = connection.cursor()

# cursor.execute("CREATE TABLE to_dos(title, duration, description)")
res = cursor.execute("SELECT name FROM sqlite_master")
res.fetchone()


class ToDoApp:
    def __init__(self):

        self.root = ttk.Window(themename="darkly")
        self.root.title("To-Do List")

        # New entry for To-Do

        self.to_do_label = ttk.Label(text="To-do Today:")
        self.to_do_label.grid(column=0, row=0, columnspan=2, padx=10, pady=5)

        self.to_do_text = ttk.Entry()
        self.to_do_text.config(width=25)
        self.to_do_text.grid(column=0, row=1, columnspan=2, padx=10, pady=5)

        self.to_do_label = ttk.Label(text="How long will it take in")
        self.to_do_label.grid(column=0, row=2, columnspan=2, padx=10)

        self.hours_label = ttk.Label(text="Hours:")
        self.hours_label.grid(column=0, row=3, padx=10, pady=10)
        self.hour_scroll = ttk.Spinbox(from_=0, to=4)
        self.hour_scroll.config(width=5)
        self.hour_scroll.insert(0, "0")
        self.hour_scroll.grid(column=0, row=4, padx=10, pady=5)

        self.minutes_label = ttk.Label(text="Minutes:")
        self.minutes_label.grid(column=1, row=3, padx=10, pady=5)
        self.min_scroll = ttk.Spinbox(from_=0, to=59)
        self.min_scroll.config(width=5)
        self.min_scroll.insert(0, "00")
        self.min_scroll.grid(column=1, row=4, padx=10, pady=5)

        self.description_label = ttk.Label(text="Description (Optional):")
        self.description_label.grid(column=0, row=5, columnspan=2, padx=10, pady=5)

        self.description_text = ttk.Text()
        self.description_text.config(width=25, height=15)
        self.description_text.grid(column=0, row=6, columnspan=2, padx=10, pady=5)

        self.b1 = ttk.Button(text="Submit", bootstyle="success", command=self.add_to_do)
        self.b1.grid(column=0, row=7, padx=10, pady=5)

        self.search_b2 = ttk.Button(text="Got time?", bootstyle="warning-outline", command=self.got_time)
        self.search_b2.grid(column=0, row=8, padx=10, pady=5)

        self.search_b4 = ttk.Button(text="Search", bootstyle="warning",)
        self.search_b4.grid(column=1, row=7, padx=10, pady=5)

        self.delete_b3 = ttk.Button(text="Delete", bootstyle="danger-outline", command=self.delete)
        self.delete_b3.grid(column=1, row=8, padx=10, pady=5)
        label_row = 0

        for row in cursor.execute("SELECT title, duration FROM to_dos ORDER BY duration"):
            print(row)
            self.to_do_label_title = ttk.Label(text=f"")
            self.to_do_label_time = ttk.Label(text=f"")
            self.to_do_label_title.grid(column=3, row=label_row, padx=10, pady=5)
            self.to_do_label_time.grid(column=4, row=label_row, padx=10, pady=5)
            label_row += 1
        self.list_todos()


    def add_to_do(self):
        print("ok, its done")
        todo_name = self.to_do_text.get()
        hour = int(self.hour_scroll.get())
        minute = int(self.min_scroll.get())
        time = f"{hour}.{minute}"
        text = self.description_text.get("1.0", END)
        to_add = (f"{todo_name}", time, str(text))
        cursor.execute("INSERT INTO to_dos VALUES(?, ?, ?)", to_add)
        connection.commit()
        self.to_do_text.delete(0, END)
        self.hour_scroll.set(0)
        self.min_scroll.set(00)
        self.description_text.delete("1.0", END)
        self.list_todos()

    def got_time(self):
        search_hour = int(self.hour_scroll.get())
        search_min = int(self.min_scroll.get())
        search_time = search_hour + (search_min / 100)
        all_times = []
        for row in cursor.execute("SELECT duration, title, description FROM to_dos ORDER BY duration DESC"):
            duration = float(row[0])
            all_times.append(duration)
            if float(row[0]) <= search_time:
                messagebox.showinfo(title=row[1], message=f"You can {row[2]}.\n It should take around {row[0]}h.")
                break
        if float(all_times[-1]) > search_time:
            messagebox.showinfo(title="Found nothing",
                                message="You do not have enough time for anything on your list")

        self.hour_scroll.set(0)
        self.min_scroll.set(00)
        self.list_todos()

    def delete(self):
        to_delete = str(self.to_do_text.get())
        sql = 'DELETE FROM to_dos WHERE title=?'
        cur = connection.cursor()
        cur.execute(sql, (to_delete,))
        connection.commit()

        self.list_todos()

    def list_todos(self):
        self.to_do_label_title.destroy()
        self.to_do_label_time.destroy()
        label_row = 0
        for row in cursor.execute("SELECT title, duration FROM to_dos ORDER BY duration"):
            print(row)

            self.to_do_label_title = ttk.Label(text=f"")
            self.to_do_label_title.config(text=f"")
            self.to_do_label_title.config(text=f"{row[0]}")
            self.to_do_label_title.grid(column=3, row=label_row, padx=10, pady=5)

            self.to_do_label_time = ttk.Label(text=f"")
            self.to_do_label_time.config(text=f"")
            self.to_do_label_time.config(text=f"{row[1]}h")
            self.to_do_label_time.grid(column=4, row=label_row, padx=10, pady=5)
            label_row += 1


if __name__ == "__main__":
    todo = ToDoApp()
    todo.root.mainloop()


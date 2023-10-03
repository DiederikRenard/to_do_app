import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook
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


class ToDoApp():

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
        self.hour_scroll.grid(column=0, row=4, padx=10, pady=5)

        self.minutes_label = ttk.Label(text="Minutes:")
        self.minutes_label.grid(column=1, row=3, padx=10, pady=5)
        self.min_scroll = ttk.Spinbox(from_=0, to=59)
        self.min_scroll.config(width=5)
        self.min_scroll.grid(column=1, row=4, padx=10, pady=5)

        self.description_label = ttk.Label(text="Description (Optional):")
        self.description_label.grid(column=0, row=5, columnspan=2, padx=10, pady=5)

        self.description_text = ttk.Text()
        self.description_text.config(width=25, height=15)
        self.description_text.grid(column=0, row=6, columnspan=2, padx=10, pady=5)

        self.b1 = Button(text="Submit", command=self.add_to_do)
        self.b1.grid(column=1, row=7, padx=10, pady=5)

        # Search for To-Do

        self.got_time_label = ttk.Label(text="Got time?")
        self.got_time_label.grid(column=3, row=0, columnspan=2, padx=10, pady=5)

        self.got_time_label = ttk.Label(text="How long do you have")
        self.got_time_label.grid(column=3, row=2, columnspan=2, padx=10)

        self.search_hours_label = ttk.Label(text="Hours:")
        self.search_hours_label.grid(column=3, row=3, padx=10, pady=10)
        self.search_hour_scroll = ttk.Spinbox(from_=0, to=4)
        self.search_hour_scroll.config(width=5)
        self.search_hour_scroll.grid(column=3, row=4, padx=10, pady=5)

        self.search_minutes_label = ttk.Label(text="Minutes:")
        self.search_minutes_label.grid(column=4, row=3, padx=10, pady=5)
        self.search_min_scroll = ttk.Spinbox(from_=0, to=59)
        self.search_min_scroll.config(width=5)
        self.search_min_scroll.grid(column=4, row=4, padx=10, pady=5)

        self.search_description_label = ttk.Label(text="Description:")
        self.search_description_label.grid(column=3, row=5, columnspan=2, padx=10, pady=5)

        self.search_description_text = ttk.Canvas()
        self.search_description_text.config(width=25, height=15)
        self.search_description_text.grid(column=3, row=6, columnspan=2, padx=10, pady=5)

        self.search_b2 = ttk.Button(text="Search")
        self.search_b2.grid(column=3, row=7, padx=10, pady=5)

    def add_to_do(self):
        print("ok, its done")
        todo_name = self.to_do_text.get()
        hour = int(self.hour_scroll.get())
        minute = int(self.min_scroll.get())
        text = self.description_text.get("1.0", END)
        new_to_do = {
            todo_name: {
                "time": [hour, minute],
                "message": text,
            }
        }
        try:
            with open("todo.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("todo.json", "w") as data_file:
                json.dump(new_to_do, data_file, indent=4)
        else:
            data.update(new_to_do)
            with open("todo.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            self.to_do_text.delete(0, END)
            self.hour_scroll.delete(0, END)
            self.min_scroll.delete(0, END)
            self.description_text.delete("1.0", END)


if __name__ == "__main__":
    app = ToDoApp()
    app.root.mainloop()

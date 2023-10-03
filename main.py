from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Concept: create a program that in which you can add to-dos,
#           estimate the time it will take and ask for suggestions when you have time
#           use TKinter!

# TODO: make window which takes name, time estimate and perhaps priority estimate

# TODO save data to a document (no database needed)

# TODO create suggest function to search for to-dos

# TODO create delete function to erase to-dos that are to-done

root = ttk.Window(themename="superhero")
root.title("To-Do Today")
root.geometry("400x600")

# New entry for To-Do

to_do_label = ttk.Label(text="To-do Today:")
to_do_label.grid(column=0, row=0, columnspan=2, padx=10, pady=5)

to_do_text = ttk.Entry()
to_do_text.config(width=25)
to_do_text.grid(column=0, row=1, columnspan=2, padx=10, pady=5)

to_do_label = ttk.Label(text="How long will it take in")
to_do_label.grid(column=0, row=2, columnspan=2, padx=10)

hours_label = ttk.Label(text="Hours:")
hours_label.grid(column=0, row=3, padx=10, pady=10)
hour_scroll = ttk.Spinbox(from_=0, to=4)
hour_scroll.config(width=5)
hour_scroll.grid(column=0, row=4, padx=10, pady=5)

minutes_label = ttk.Label(text="Minutes:")
minutes_label.grid(column=1, row=3, padx=10, pady=5)
min_scroll = ttk.Spinbox(from_=0, to=59)
min_scroll.config(width=5)
min_scroll.grid(column=1, row=4, padx=10, pady=5)

description_label = ttk.Label(text="Description (Optional):")
description_label.grid(column=0, row=5, columnspan=2, padx=10, pady=5)

description_text = ttk.Text()
description_text.config(width=25, height=15)
description_text.grid(column=0, row=6, columnspan=2, padx=10, pady=5)

b1 = ttk.Button(text="Submit", bootstyle="success")
b1.grid(column=1, row=7, padx=10, pady=5)

# Search for To-Do



to_do_label = ttk.Label(text="Got time?")
to_do_label.grid(column=3, row=0, columnspan=2, padx=10, pady=5)


to_do_label = ttk.Label(text="How long do you have in")
to_do_label.grid(column=3, row=2, columnspan=2, padx=10)

hours_label = ttk.Label(text="Hours:")
hours_label.grid(column=3, row=3, padx=10, pady=10)
hour_scroll = ttk.Spinbox(from_=0, to=4)
hour_scroll.config(width=5)
hour_scroll.grid(column=3, row=4, padx=10, pady=5)

minutes_label = ttk.Label(text="Minutes:")
minutes_label.grid(column=4, row=3, padx=10, pady=5)
min_scroll = ttk.Spinbox(from_=0, to=59)
min_scroll.config(width=5)
min_scroll.grid(column=4, row=4, padx=10, pady=5)

description_label = ttk.Label(text="Description:")
description_label.grid(column=3, row=5, columnspan=2, padx=10, pady=5)

description_text = ttk.Canvas()
description_text.config(width=25, height=15)
description_text.grid(column=3, row=6, columnspan=2, padx=10, pady=5)

b1 = ttk.Button(text="Submit", bootstyle="success")
b1.grid(column=1, row=7, padx=10, pady=5)

b2 = ttk.Button(text="Search", bootstyle="info-outline")
b2.grid(column=3, row=7, padx=10, pady=5)

root.mainloop()
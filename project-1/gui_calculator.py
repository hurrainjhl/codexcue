import tkinter as tk
from tkinter import messagebox
import math


def click(event):
    current = display.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            display.delete(0, tk.END)
    elif button_text == "C":
        display.delete(0, tk.END)
    elif button_text == "CE":
        display.delete(0, tk.END)
    elif button_text == "⌫":
        display.delete(len(current) - 1, tk.END)
    elif button_text == "1/x":
        try:
            result = 1 / float(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            display.delete(0, tk.END)
    elif button_text == "x²":
        try:
            result = float(current) ** 2
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            display.delete(0, tk.END)
    elif button_text == "²√x":
        try:
            result = math.sqrt(float(current))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            display.delete(0, tk.END)
    elif button_text == "±":
        if current:
            if current[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
    else:
        display.insert(tk.END, button_text)


app = tk.Tk()
app.title("Scientific Calculator")

# Display
display = tk.Entry(app, font=("Arial", 18), borderwidth=5, relief=tk.SUNKEN)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Button Configuration
buttons = [
    ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('⌫', 1, 3),
    ('1/x', 2, 0), ('x²', 2, 1), ('²√x', 2, 2), ('/', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
    ('±', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(app, text=text, font=("Arial", 18), padx=20, pady=20)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", click)

# Adjust grid layout to resize buttons
for i in range(7):
    app.grid_rowconfigure(i, weight=1)
for i in range(4):
    app.grid_columnconfigure(i, weight=1)

app.mainloop()

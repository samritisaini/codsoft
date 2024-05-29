import tkinter as tk

def add_to_calculation(symbol):
    text_result.insert(tk.END, str(symbol))

def evaluate_calculation():
    try:
        result = str(eval(text_result.get("1.0", tk.END).strip()))
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, result)
    except:
        clear_field()
        text_result.insert(tk.END, "error")

def clear_field():
    text_result.delete("1.0", tk.END)

root = tk.Tk()
root.geometry("300x275+100+200")
root.title("Simple Calculator")

label_result = tk.Label(root, width=25, height=2, text=" ", font=("Arial", 30))
label_result.pack()

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

buttons = [
    ("1", 2, 1), ("2", 2, 2), ("3", 2, 3), ("4", 3, 1), ("5", 3, 2), 
    ("6", 3, 3), ("7", 4, 1), ("8", 4, 2), ("9", 4, 3), ("0", 5, 2), 
    ("+", 2, 4), ("-", 3, 4), ("*", 4, 4), ("/", 5, 4), ("(", 5, 1), 
    (")", 5, 3), ("C", 6, 1), ("=", 6, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, width=5, font=("Arial", 14))
    button.grid(row=row, column=column)
    button.config(command=lambda button_text=button_text: button_click(button_text))

def button_click(symbol):
    if symbol == "=":
        evaluate_calculation()
    elif symbol == "C":
        clear_field()
    else:
        add_to_calculation(symbol)

root.mainloop()

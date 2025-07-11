import tkinter as tk

def click(event): # exp
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry widget
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify="right", fg="black")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(row_frame, text=btn, font="Arial 18", relief=tk.GROOVE, border=1, bg="red", fg="white")
        b.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        b.bind("<Button-1>", click)

root.mainloop()

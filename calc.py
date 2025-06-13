import tkinter as tk

window = tk.Tk()
window.title("My Calculator")

window.geometry("500x500")

# Validating input
def validateInput(new_value):
    allowed = "1234567890.+-x/"
    return all(char in allowed for char in new_value)
vcmd = (window.register(validateInput), "%P")

entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief="solid",justify="right", validate="key",validatecommand= vcmd)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout

buttons = [
    ['CE', 'C', '', ''],
    ['7', '8', '9', '/'],
    ['4', '5', '6', 'x'],
    ['1', '2', '3', '+'],
    ['0', '.', '-', '=']
]

def on_button_click(ch):
    if ch == "=":
        expression = entry.get().replace('x', '*')
        try:
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif ch == "C":
        entry.delete(0, tk.END)
    elif ch == "DEL":
        for i in range(len(text)-1, -1, -1):
            entry.delete(i+1, tk.END)
            break
    elif ch == "CE":
        text = entry.get()
        for i in range(len(text)-1, -1, -1):
            if text[1] in "+-x/":
                entry.delete(i+1, tk.END)
                break
            else:
                entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, ch)

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        tk.Button(window, text=char, width = 5, height = 2, font=('Arial', 18), command=lambda ch=char: on_button_click(ch)).grid(row= r+2, column=c, padx=5, pady=5)

window.mainloop()
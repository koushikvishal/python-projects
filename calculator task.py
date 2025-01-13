import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry widget for display
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.SUNKEN, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
button_text = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]

# Adding buttons to the window
for row in button_text:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for text in row:
        button = tk.Button(frame, text=text, font="Arial 18", relief=tk.RAISED, borderwidth=3)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", on_click)

# Run the application
root.mainloop()
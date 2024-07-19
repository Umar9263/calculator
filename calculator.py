import tkinter as tk

def on_click(event):
    current_text = result_label["text"]
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_label.config(text=str(result))
        except Exception as e:
            result_label.config(text="Error")
    elif button_text == "C":
        result_label.config(text="")
    else:
        result_label.config(text=current_text + button_text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Create the result label
result_label = tk.Label(root, text="", font=("Arial", 24))
result_label.pack(fill=tk.BOTH, expand=True)

# Create the buttons
button_texts = [
    ("7", "8", "9", "+"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "*"),
    ("C", "0", "=", "/"),
]

for row_items in button_texts:
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.BOTH, expand=True)

    for text in row_items:
        button = tk.Button(button_frame, text=text, font=("Arial", 18), relief=tk.RIDGE)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

# Start the application
root.mainloop()

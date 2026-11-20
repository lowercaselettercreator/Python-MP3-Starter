import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

tk.Label(window, text="Top", bg="lightblue").pack(fill="y")
tk.Label(window, text="Middle", bg="lightgreen").pack(fill="both", anchor="s")
tk.Label(window, text="Bottom", bg="lightpink").pack(fill="y")

button_row = tk.Frame(window)
button_row.pack(pady=10)

tk.Button(button_row, text="OK").pack(side="left", padx=5)
tk.Button(button_row, text="Cancel").pack(side="left", padx=5)

window.mainloop()
import customtkinter as ctk
import tkinter as tk

def calculate_morels():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = 30

    result = (num3 - num2) * num1
    stacks = 0
    rows = 0

    result_label.config(text=f"Overall Morels: {result}")

    while result >= 240:
        result = result - 240
        rows += 1

    while result >= 30:
        result = result - 30
        stacks += 1

    rows_label.config(text=f"Rows of Morels: {rows}")
    stacks_label.config(text=f"Stacks of Morels: {stacks}")
    single_morels_label.config(text=f"Single Morels: {result}")

# Utwórz główne okno aplikacji
root = ctk.CTk()
root.title("Morel Mushroom Calculator")
root.configure(theme="dark")  # Ustaw ciemny motyw

# Etykiety
label1 = tk.Label(root, text="Enter your glow worm farm count:")
label2 = tk.Label(root, text="Enter how many morels left inside:")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

# Pola do wprowadzania danych
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

# Przycisk do obliczeń (standardowy przycisk tkinter)
calculate_button = tk.Button(root, text="Calculate", command=calculate_morels)
calculate_button.grid(row=2, columnspan=2)

# Wyświetlanie wyników (standardowe etykiety tkinter)
result_label = tk.Label(root, text="Overall Morels: ")
rows_label = tk.Label(root, text="Rows of Morels: ")
stacks_label = tk.Label(root, text="Stacks of Morels: ")
single_morels_label = tk.Label(root, text="Single Morels: ")

result_label.grid(row=3, columnspan=2)
rows_label.grid(row=4, columnspan=2)
stacks_label.grid(row=5, columnspan=2)
single_morels_label.grid(row=6, columnspan=2)

# Rozpocznij pętlę główną aplikacji
root.mainloop()
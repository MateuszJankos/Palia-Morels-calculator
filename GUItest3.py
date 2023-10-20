import customtkinter
import tkinterDnD

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("400x500")
app.title("Morel Calculator")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Palia morel calculator")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Glow Worm count")
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Morels left inside")
entry_2.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Rows of Morels: 0", fg_color="transparent", pady=10, padx=10)
label_2.pack()

label_3 = customtkinter.CTkLabel(master=frame_1, text="Stacks of Morels: 0", fg_color="transparent", pady=10, padx=10)
label_3.pack()

label_4 = customtkinter.CTkLabel(master=frame_1, text="Single Morels: 0", fg_color="transparent", pady=10, padx=10)
label_4.pack()

label_5 = customtkinter.CTkLabel(master=frame_1, text="Overall Morels: 0", fg_color="transparent", pady=10, padx=10)
label_5.pack()

def calculate_morels():
    num1 = float(entry_1.get())
    num2 = float(entry_2.get())
    num3 = 30

    result = (num3 - num2) * num1
    stacks = 0
    rows = 0

    while result >= 240:
        result = result - 240
        rows += 1

    while result >= 30:
        result = result - 30
        stacks += 1

    label_2.configure(text=f"Rows of Morels: {rows}")
    label_3.configure(text=f"Stacks of Morels: {stacks}")
    label_4.configure(text=f"Single Morels: {result}")
    label_5.configure(text=f"Overall Morels: {rows * 240 + stacks * 30 + result}")

button_1 = customtkinter.CTkButton(master=frame_1, command=calculate_morels, text="Calculate")
button_1.pack(pady=10, padx=10)

def reset_results():
    label_2.configure(text="Rows of Morels: 0")
    label_3.configure(text="Stacks of Morels: 0")
    label_4.configure(text="Single Morels: 0")
    label_5.configure(text="Overall Morels: 0")
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")

reset_button = customtkinter.CTkButton(master=frame_1, command=reset_results, text="Reset")
reset_button.pack(pady=50, padx=10)

app.mainloop()

import customtkinter
import tkinterDnD

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x500")
app.title("Morel Calculator")

print(type(app), isinstance(app, tkinterDnD.Tk))

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Palia morel calculator")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Glow Worm count")
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Morels left inside")
entry_2.pack(pady=10, padx=10)

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

button_1 = customtkinter.CTkButton(master=frame_1, command=calculate_morels, text="Calculate")
button_1.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Rows of Morels: {rows}", fg_color="transparent",pady=10, padx=10).bind(command=calculate_morels)

label_3 = customtkinter.CTkLabel(master=frame_1, text="Stacks of Morels: {stacks}", fg_color="transparent",pady=10, padx=10).bind(command=calculate_morels)

label_4 = customtkinter.CTkLabel(master=frame_1, text="Single Morels: {result}", fg_color="transparent",pady=10, padx=10).bind(command=calculate_morels)

label_5 = customtkinter.CTkLabel(master=frame_1, text="Overall Morels: {result}", fg_color="transparent",pady=10, padx=10).bind(command=calculate_morels)

app.mainloop()
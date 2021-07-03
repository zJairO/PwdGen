from tkinter import *
import random, string
import pyperclip
from tkinter import ttk
from ttkbootstrap import Style

# Style
style = Style(theme = 'cyborg')
root = style.master

#root = Tk()
root.geometry("400x230")
root.resizable(0, 0)
root.title("Pwd Gen")

# Logo
logo = PhotoImage(file = "res/logo.png")

# Icon
icon = PhotoImage(file = "res/lock.png")
root.iconphoto(False, icon)

# Label
Label(root, image = logo).pack(pady = 5)

pass_str = StringVar()

# Función generar pwd
def generator():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbol = string.punctuation

    # Mezclar data
    all = lower + upper + num + symbol

    # Randomizer
    temp = random.sample(all, 16)

    # Create password
    password = "".join(temp)

    # Pass String
    pass_str.set(password)

# Función copiar pwd
def copyPassword():
    pyperclip.copy(pass_str.get())

# Botones & Entry
ttk.Entry(root, textvariable = pass_str, width = 27, justify = CENTER).pack(pady = 5)
ttk.Button(root, text = "GENERATE PASSWORD", command = generator, width = 25, style='success.TButton').pack(pady = 5)
ttk.Button(root, text = 'COPY TO CLIPBOARD', command = copyPassword, width = 25, style='secondary.TButton').pack(pady = 5)

# Run
root.mainloop()
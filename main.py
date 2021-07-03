from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("400x220")
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
Entry(root, textvariable = pass_str, width = 23, justify = CENTER).pack(pady = 5)
Button(root, text = "GENERATE PASSWORD", command = generator, width = 20).pack(pady = 5)
Button(root, text = 'COPY TO CLIPBOARD', command = copyPassword, width = 20).pack(pady = 5)

# Run
root.mainloop()
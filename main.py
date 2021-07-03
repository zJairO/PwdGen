from tkinter import *
from tkinter import ttk, simpledialog, messagebox
from ttkbootstrap import Style
import random, string, pyperclip, shutil, datetime, os

class App:
    def __init__(self):
        # Init
        self.style = Style(theme = "cyborg")
        self.root = self.style.master
        self.root.geometry("400x230")
        self.root.resizable(0, 0)
        self.root.title("Pwd Gen")
        self.icon = PhotoImage(file = "res/lock.png")
        self.root.iconphoto(False, self.icon)
        # Menubar
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        # File
        filemenu = Menu(menubar)
        filemenu.add_command(label = "Save Current Password", command = self.savepwd)
        menubar.add_cascade(label="File", menu = filemenu)
        # Manage
        managemenu = Menu(menubar)
        managemenu.add_command(label = "Export Passwords", command = self.exportpwd)
        #managemenu.add_command(label = "Import Passwords", command = self.importpwd)
        #managemenu.add_command(label = "Remove Passwords")
        #managemenu.add_command(label = "Remove Backups")
        menubar.add_cascade(label="Manage", menu = managemenu)
        # External
        #externalmenu = Menu(menubar)
        #externalmenu.add_command(label = "Send Passwords to Email", command = self.emailpwd)
        #menubar.add_cascade(label="External", menu = externalmenu)
        # About
        #helpmenu = Menu(menubar)
        #helpmenu.add_command(label = "About", command = self.helppwd)
        #menubar.add_cascade(label="Help", menu = helpmenu)
        # Body
        logo = PhotoImage(file = "res/logo.png")
        Label(self.root, image = logo).pack(pady = 5)
        self.pass_str = StringVar()
        # Buttons & Entry
        self.genpassword()
        ttk.Entry(self.root, textvariable = self.pass_str, width = 27, justify = CENTER).pack(pady = 5)
        ttk.Button(self.root, text = "GENERATE PASSWORD", command = self.genpassword, width = 25, style='success.TButton').pack(pady = 5)
        ttk.Button(self.root, text = 'COPY TO CLIPBOARD', command = self.copyPassword, width = 25, style='secondary.TButton').pack(pady = 5)
        # Loop
        self.root.mainloop()

    def genpassword(self):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbol = string.punctuation
        # Mix data
        all = lower + upper + num + symbol
        # Randomizer
        temp = random.sample(all, 16)
        # Create password
        password = "".join(temp)
        # Pass Variable
        self.pass_str.set(password)

    def savepwd(self):
        # Get pwd
        pwd = self.pass_str.get()
        pwd_desc = simpledialog.askstring(title = "Pwd Gen", prompt="Enter your Password Description:", )
        if pwd_desc is not None and len(pwd_desc) > 0:
            with open ("pwd", "a") as file:
                file.write(f"{pwd_desc} {pwd}\n")
                messagebox.showinfo(message=f"Success!\nWe have saved:\nPassword {pwd}\nDescription {pwd_desc}", title="Pwd Gen")
    
    def exportpwd(self):
        now = datetime.datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        dir_location = os.getcwd()
        shutil.copyfile("pwd", f"{dt_string}_backup.txt")
        messagebox.showinfo(message = f"Success, find your backup on:\n{dir_location}/{dt_string}_backup.txt", title="Pwd Gen")

    def copyPassword(self):
        pyperclip.copy(self.pass_str.get())

MyApp = App()
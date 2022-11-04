from tkinter import *
from customtkinter import *
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class Main(CTk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.minsize(1000,580)
        self.resizable(False,False)
        self.configure(bg="#02080d")
        self.iconbitmap("img/icon.ico")

        self.frame_login = CTkFrame(self,width=435,height=310,border_color="#df2d00",border_width=1.5)

        self.entry_username = CTkEntry(master=self.frame_login,placeholder_text="Enter your username",width=210,height=35,corner_radius=12)
        self.entry_password = CTkEntry(master=self.frame_login,placeholder_text="Enter your password",width=210,height=35,corner_radius=12,show="*")
        self.login_button = CTkButton(master=self.frame_login,text="Log In",fg_color="#290f0b",text_color="#fff4d6",hover_color="#441912",corner_radius=12,command=self.LogIn)

        self.frame_login.place(x=285,y=110)
        self.entry_username.place(x=110,y=85)
        self.entry_password.place(x=110,y=160)
        self.login_button.place(x=137,y=217)

    def LogIn(self):
        self.entry_username_get = self.entry_username.get()
        self.entry_password_get = self.entry_password.get()

        self.list_username:str = ["Sebastian Kučera"]
        self.list_password:int = ["7259"]

        for self.item_username in self.list_username:
            for self.item_password in self.list_password:
                if self.item_username == self.entry_username_get and self.item_password == self.entry_password_get:
                    messagebox.showinfo("Login Form","Your data is valid")
                    break
                else:
                    messagebox.showerror("Login Form","Your data is not valid")
                    break
                    
root = Main()
root.mainloop()
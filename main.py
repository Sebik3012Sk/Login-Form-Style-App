from tkinter import *
from customtkinter import *
from tkinter import messagebox as msg
from PIL import Image , ImageTk
import customtkinter as customtkpro
from sys import argv
import platform as platfm
import random as rd
import math as mth
import tkinter as tk
import smtplib


mode = argv[1]
mode_color = argv[2]

customtkpro.set_appearance_mode(mode)
customtkpro.set_default_color_theme(mode_color)
customtkpro.set_widget_scaling(1.05) 


class Main(CTk):
    def __init__(self):
        super().__init__()

        WIDTH = 1000
        HEIGHT = 580

        self.pos_w_x = 150
        self.pos_w_y = 50

        
        self.title("Restaurant Order Menu")
        self.geometry(f"{WIDTH}x{HEIGHT}+{self.pos_w_x}+{self.pos_w_y}")
        self.resizable(False,False)
        self.configure(bg="#02080d")
        self.attributes("-alpha",1)
        self.iconbitmap("img/icon.ico")
        

        self.overrideredirect(False)

        self.frame_login = CTkFrame(self,width=435,height=310,border_color="#ff2020",border_width=2.5)
        
        self.list_data = []

        self.header_frame_label = CTkLabel(master=self.frame_login,text="Login Form",text_font=("italic",23),text_color="white")
        self.entry_username = CTkEntry(master=self.frame_login,placeholder_text="Enter your username",width=210,height=35,corner_radius=12,justify="center")
        self.entry_password = CTkEntry(master=self.frame_login,placeholder_text="Enter your password",width=210,height=35,corner_radius=12,show="*",justify="center")
        self.login_button = CTkButton(master=self.frame_login,text="Log In",fg_color="#970000",text_color="#fff4d6",hover_color="#db0000",corner_radius=12,command=self.LogIn)
        self.forgot_password = CTkButton(master=self.frame_login,text="forgot password",text_color="white",fg_color="#b90000",hover_color="#fd0000",width=35,corner_radius=13,command=self.newForgotPasswordW)

        self.frame_login.place(x=285,y=110)
        self.header_frame_label.place(x=139.7,y=27)
        self.entry_username.place(x=110,y=85)
        self.entry_password.place(x=110,y=160)
        self.login_button.place(x=137,y=217)
        self.forgot_password.place(x=150,y=265)

    def update(self):
        self.aboutComputerData()
        self.get_data()
        self.keys_listeners()

	 
    def get_data(self):
        self.data_user = "[APP] User joined to program"
        print(self.data_user)

    def enter_bind(self , event):
        self.LogIn()
        print(event)

    def keys_listeners(self):
        self.bind("<Return>",self.enter_bind)


    def aboutComputerData(self):

        self.list = [platfm.node(),platfm.system() + " " + platfm.release()]

        self.file = "platform.txt"

        with open(self.file,"w") as file:
            for self.item in self.list:
                file.write(self.item + "\n")
 

    def removeWindowItems(self):
        self.frame_login.place_forget()
        self.entry_username.place_forget()
        self.entry_password.place_forget()
        self.login_button.place_forget()

    def optionMenu(self , choise):
        self.x = 265
        self.y = 135

        self.x2 = 300
        self.y2 = 385

        if choise == self.values[0]:
            self.inputDialog = CTkInputDialog(master=self,title="Food Menu",text="Select tipe of the pizza",fg_color="#ec0000",hover_color="#ff2020",border_color="#ff0f0f")
            self.button_order = CTkButton(master=self,text="order",image=self.order_image,text_font="Helvetica",text_color="white",fg_color="#a80000",hover_color="#ca0000")
            self.button_order.place(x=self.x2,y=self.y2)
            self.choose = self.inputDialog.get_input()
            
            self.list_of_image = []

            self.list_of_image.append(self.list_of_foodImg[0])


            for self.item in self.list_of_image:
                self.label = Label(master=root,image=self.item)
                self.label.place(x=self.x,y=self.y)

        elif(choise == self.values[1]):
            self.inputDialog = CTkInputDialog(master=self,title="Food Menu",text="Select how meat do you want \n to your soup",fg_color="#ec0000",hover_color="#ff2020",border_color="#ff0f0f")
            self.button_orders = CTkButton(master=self,text="order",image=self.order_image,text_color="white",text_font="Helvetica",fg_color="#a80000",hover_color="#ca0000")
            self.button_orders.place(x=self.x2 + 268,y=self.y2)
            self.choose = self.inputDialog.get_input()
            self.list_of_image = []

            self.list_of_image.append(self.list_of_foodImg[1])


            for self.item in self.list_of_image:
                self.img_label = Label(master=root,image=self.item)
                self.img_label.place(x=self.x + 255,y=self.y)

        

    def unLogin(self):
        self.text_user_unlogin = f"[APP] User {self.entry_username_get} unlogin from app menu"
        print(self.text_user_unlogin)

        self.frame_login.place(x=285,y=110)
        self.entry_username.place(x=110,y=85)
        self.entry_password.place(x=110,y=160)
        self.login_button.place(x=137,y=217)

        self.username_box.place_forget()
        self.quit_button.place_forget()
        self.label_heading.place_forget()
        self.otpion_menu.place_forget()

        try:
            self.label.place_forget()
            self.img_label.place_forget()
            self.button_order.place_forget()
            self.button_orders.place_forget()
        except:
            pass
            

    def newStuctureWindow(self):
        

        self.text_user = f"[APP] User {self.entry_username_get} joined to menu"
        print(self.text_user)

        # loading images
        self.pizza_image = ImageTk.PhotoImage(Image.open("img/pizza.jpeg"))
        self.vegetale_soup = ImageTk.PhotoImage(Image.open("img/Vegetable Soup.jpg"))
        self.order_image = ImageTk.PhotoImage(Image.open("img/order-icon.png"))
        self.account_image = ImageTk.PhotoImage(Image.open("img/account-image.png"))
        self.quit_image = ImageTk.PhotoImage(Image.open("img/quit-image.png"))

        self.list_of_foodImg = [self.pizza_image,self.vegetale_soup]
        self.values = ["Pizza","Vegetable Soup","Cheese Cake","Chips and Fish"]

        self.username_box = CTkButton(master=self,text=self.entry_username_get,fg_color="#ff2020",hover_color="#ff0f0f",image=self.account_image)
        self.quit_button = CTkButton(master=self,image=self.quit_image,text="",width=25,height=13,corner_radius=15,fg_color="#fd0000",hover_color="#ff0f0f",command=self.unLogin)
        self.label_heading = CTkLabel(master=self,text=f"Welcome in Our Restaurant Menu {self.entry_username_get}",text_font="Helvetica")
        self.otpion_menu = CTkOptionMenu(master=self,values=self.values,fg_color="#b63111",button_hover_color="#d53a14",dropdown_hover_color="#d53a14",button_color="#b63111",dropdown_color="#b63111",command=self.optionMenu)

        self.username_box.place(x=35,y=35)
        self.quit_button.place(x=207,y=31)
        self.label_heading.place(x=315,y=18)
        self.otpion_menu.place(x=410,y=75)


    def newForgotPasswordW(self):
        self.removeWindowItems()

        self.header_text = CTkLabel(master=self,text="Forgot Password",text_font=("italic",22))
        self.entry_email = CTkEntry(master=self,placeholder_text="Enter your email",text_font=("italic",10),width=275,height=35,corner_radius=13,justify="center")
        self.entry_code = CTkEntry(master=self,placeholder_text="Enter your code",text_font=("italic",11),width=275,height=35,corner_radius=13,justify="center") 
        self.send_button = CTkButton(master=self,text="confirm",text_font=("italic",10),fg_color="#ff2020",hover_color="#ff0f0f",command=self.forget_password)

        self.header_text.place(x=380,y=25)
        self.entry_email.place(x=350,y=80)
        self.entry_code.place(x=350,y=145)
        self.send_button.place(x=412,y=195)

    def forget_password(self):

        self.send_button["text"] = "Ověřit"

        self.email_send = "sebastian30kucera@gmail.com"
        self.password = "drqziqzkajlemgqx"
        self.receiver = self.entry_email.get()
        self.code = rd.randint(4600,8200)
        self.message = f"Subject: Account Get\n\n Here is your code to account : {self.code}"
        

        with smtplib.SMTP(host="smtp.gmail.com",port=587) as self.connection:
            self.connection.starttls()
            self.connection.login(self.email_send,self.password)
            self.connection.sendmail(from_addr=self.email_send,to_addrs=self.receiver,msg=self.message.encode("utf-8"))
            

        if self.entry_code.get() == self.code:
            try:
                self.connection = None
            except:
                pass

            return self.newStuctureWindow()

    def LogIn(self):
        self.entry_username_get = self.entry_username.get()
        self.entry_password_get = self.entry_password.get()

        self.list_username:str = ["Sebastian Kučera","Robert Kučera"]
        self.list_password:int = ["7259","1964"]

        self.entry_username.delete(0,END)

        self.entry_password.delete(0,END)

        self.save_password = []

        self.save_password.append(self.entry_password_get)

        self.i = 0

        for self.item in self.save_password:
            for self.letter_item in self.item:
                try:
                    self.data_encode_h = ord(self.letter_item) + int(rd.randint(10,50)) // int(rd.randint(1,5)) * 5 + round(pow(2,4) // mth.pow(1,3))
                    print("START ENCODE")
                    print(self.data_encode_h)
                    print("STOP ENCODE")
                    print("START DECODE")
                    print(chr(self.data_encode_h))
                    print("STOP DECODE")
                except tk.TclError:
                    pass
                finally:
                    self.data_encode_h = ord(self.letter_item) + int(rd.randint(10,50)) // int(rd.randint(1,5)) * int(rd.randint(0,6)) - 5 + round(pow(2,4))
                    print("START ENCODE")
                    print(self.data_encode_h)
                    print("STOP ENCODE")
                    print("START DECODE")
                    print(chr(self.data_encode_h))
                    print("STOP DECODE")

        with open("data_list.txt","r+") as self.file:
            self.r_data = f"Username : {self.entry_username_get} \nPassword : {self.entry_password_get}\n"

            self.list_data.append(self.r_data)

            for self.item in self.list_data:
                self.list_data.clear()

                self.file.write(self.item)

                self.press_enter = "\n"

                self.file.write(self.press_enter)

                if len(self.press_enter) > 1:
                    self.press_enter = ""
                    
            
        for self.item_username in self.list_username:
            for self.item_password in self.list_password:
                if self.item_username == self.entry_username_get and self.item_password == self.entry_password_get:
                    msg.showinfo("Login Form","Your data is valid")
                    self.removeWindowItems()
                    self.newStuctureWindow()
                    break
                elif(self.list_username[1] == self.entry_username_get and self.list_password[1] == self.entry_password_get):
                    msg.showinfo("Login Form","Your data is valid")
                    self.removeWindowItems()
                    self.newStuctureWindow()
                else:
                    msg.showerror("Login Form","Your data is not valid")
                    break


if __name__ == "__main__":                
    root = Main()
    root.update()
    root.mainloop()
else:
    print("Your operation system it is not good !")
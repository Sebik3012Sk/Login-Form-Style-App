from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class Main(CTk):
    def __init__(self):
        super().__init__()

        self.WIDTH = 1000
        self.HEIGHT = 580

        self.pos_w_x = 150
        self.pos_w_y = 50

        self.title("Restaurant Order Menu")
        # self.attributes("-alpha",0.1)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{self.pos_w_x}+{self.pos_w_y}")
        self.resizable(False,False)
        self.configure(bg="#02080d")
        self.iconbitmap("img/icon.ico")

        self.frame_login = CTkFrame(self,width=435,height=310,border_color="#ff2020",border_width=2.5)

        self.list_data = []

        self.entry_username = CTkEntry(master=self.frame_login,placeholder_text="Enter your username",width=210,height=35,corner_radius=12)
        self.entry_password = CTkEntry(master=self.frame_login,placeholder_text="Enter your password",width=210,height=35,corner_radius=12,show="*")
        self.login_button = CTkButton(master=self.frame_login,text="Log In",fg_color="#970000",text_color="#fff4d6",hover_color="#db0000",corner_radius=12,command=self.LogIn)

        self.frame_login.place(x=285,y=110)
        self.entry_username.place(x=110,y=85)
        self.entry_password.place(x=110,y=160)
        self.login_button.place(x=137,y=217)

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
            self.inputDialog = CTkInputDialog(master=self,title="Food Menu",text="Select tipe of the pizza",fg_color="#ec0000",hover_color="#ff2020")
            self.button_order = CTkButton(master=self,text="order",text_color="white",fg_color="#a80000",hover_color="#ca0000")
            self.button_order.place(x=self.x2,y=self.y2)
            self.choose = self.inputDialog.get_input()
            
            
            self.list_of_image = []

            self.list_of_image.append(self.list_of_foodImg[0])


            for self.item in self.list_of_image:
                self.label = Label(master=root,image=self.item)
                self.label.place(x=self.x,y=self.y)

        elif(choise == self.values[1]):
            self.inputDialog = CTkInputDialog(master=self,title="Food Menu",text="Select how meat do you want \n to your soup",fg_color="#ec0000",hover_color="#ff2020")
            self.button_orders = CTkButton(master=self,text="order",text_color="white",fg_color="#a80000",hover_color="#ca0000")
            self.button_orders.place(x=self.x2 + 265,y=self.y2)
            self.choose = self.inputDialog.get_input()
            self.list_of_image = []

            self.list_of_image.append(self.list_of_foodImg[1])


            for self.item in self.list_of_image:
                self.label = Label(master=root,image=self.item)
                self.label.place(x=self.x + 255,y=self.y)


    def newStuctureWindow(self):
        

        # loading images
        self.pizza_image = ImageTk.PhotoImage(Image.open("img/pizza.jpeg"))
        self.vegetale_soup = ImageTk.PhotoImage(Image.open("img/Vegetable Soup.jpg"))

        self.list_of_foodImg = [self.pizza_image,self.vegetale_soup]
        self.values = ["Pizza","Vegetable Soup","Cheese Cake","Chips and Fish"]

        self.label_heading = CTkLabel(master=self,text="Welcome in Our Restaurant Menu",text_font="Helvetica")
        self.otpion_menu = CTkOptionMenu(master=self,values=self.values,fg_color="#b63111",button_hover_color="#d53a14",dropdown_hover_color="#d53a14",button_color="#b63111",dropdown_color="#b63111",command=self.optionMenu)

        self.label_heading.place(x=375,y=18)
        self.otpion_menu.place(x=410,y=75)

        

    def LogIn(self):
        self.entry_username_get = self.entry_username.get()
        self.entry_password_get = self.entry_password.get()

        self.list_username:str = ["Sebastian Kučera"]
        self.list_password:int = ["7259"]


        with open("data_list.txt","r+") as file:
            self.r_data = f"Username : {self.entry_username_get} \nPassword : {self.entry_password_get}\n"

            self.list_data.append(self.r_data)

            for self.item in self.list_data:
                file.write(self.item)


        for self.item_username in self.list_username:
            for self.item_password in self.list_password:
                if self.item_username == self.entry_username_get and self.item_password == self.entry_password_get:
                    messagebox.showinfo("Login Form","Your data is valid")
                    self.removeWindowItems()
                    self.newStuctureWindow()
                    break
                else:
                    messagebox.showerror("Login Form","Your data is not valid")
                    break
                    
root = Main()
root.mainloop()
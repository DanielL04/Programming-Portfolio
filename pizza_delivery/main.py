# Daniel Lehman

from tkinter import *

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.config(bg="cornflowerblue")

    def create_widgets(self):
        self.lbl_name = Label(self, text = "Name:", bg="cornflowerblue")
        self.lbl_adress = Label(self, text = "Adress:", bg="cornflowerblue")
        self.lbl_phone = Label(self, text = "Phone Number:", bg="cornflowerblue")
        self.lbl_size = Label(self, text = "Size:", bg="cornflowerblue")
        self.lbl_crust = Label(self, text = "Crust:", bg="cornflowerblue")
        self.lbl_toppings = Label(self, text = "Toppings:", bg="cornflowerblue")
        self.txtbx_name = Entry(self, width = 20)
        self.txtbx_adress = Entry(self, width=20)
        self.txtbx_phone = Entry(self, width=20)
        self.size = StringVar()
        self.crust = StringVar()
        self.output = Text(self)
        self.size.set("large")
        self.crust.set("Stuffed")
        self.rbttn_size_Sm = Radiobutton(self,
                                         variable = self.size,
                                         text="Small",
                                         value="small",
                                         )
        self.rbttn_size_M = Radiobutton(self,
                                        variable = self.size,
                                        text="Medium",
                                        value="medium",
                                        )
        self.rbttn_size_L = Radiobutton(self,
                                        variable = self.size,
                                        text="Large",
                                        value="large",
                                        )
        self.rbttn_crust1 = Radiobutton(self,
                                        variable = self.crust,
                                        text="Stuffed",
                                        value="Stuffed",
                                        )
        self.rbttn_crust2 = Radiobutton(self,
                                        variable = self.crust,
                                        text="Pan",
                                        value="Pan",
                                        )
        self.rbttn_crust3 = Radiobutton(self,
                                        variable = self.crust,
                                        text="Deep",
                                        value="Deep",
                                        )
        self.rbttn_crust4 = Radiobutton(self,
                                        variable = self.crust,
                                        text="Thin",
                                        value="Thin",
                                        )
        self.rbttn_crust5 = Radiobutton(self,
                                        variable = self.crust,
                                        text="Square",
                                        value="Square",
                                        )
        self.rbttn_crust6 = Radiobutton(self,
                                        variable = self.crust,
                                        text="None",
                                        value="None",
                                        )
        self.pep =  Checkbutton(self,
                                           variable = self.crust,
                                           text="Pepperoni",
                                           )
        self.bttn_order = Button(self, text = "Order", bg="lightgreen", command = self.order)
        self.output = Text(self)
        # add widgets to the grid
        self.lbl_name.grid(row=0, column=0, sticky = NW)
        self.lbl_adress.grid(row=1, column=0, sticky =NW)
        self.lbl_phone.grid(row=2, column=0, sticky =NW)
        self.lbl_size.grid(row=3, column=0, sticky =NW)
        self.lbl_crust.grid(row=5, column=0, sticky =NW)
        self.lbl_toppings.grid(row=8, column=0, sticky=NW)
        self.txtbx_name.grid(row=0, column=1, sticky=NE)
        self.txtbx_adress.grid(row=1, column=1, sticky=NE)
        self.txtbx_phone.grid(row=2, column=1, sticky=NE)
        self.rbttn_size_Sm.grid(row=4, column=0, sticky=NW)
        self.rbttn_size_M.grid(row=4, column=1, sticky=NW)
        self.rbttn_size_L.grid(row=4, column=2, sticky=NW)
        self.rbttn_crust1.grid(row=6, column=0, sticky=NW)
        self.rbttn_crust2.grid(row=6, column=1, sticky=NW)
        self.rbttn_crust3.grid(row=6, column=2, sticky=NW)
        self.rbttn_crust4.grid(row=7, column=0, sticky=NW)
        self.rbttn_crust5.grid(row=7, column=1, sticky=NW)
        self.rbttn_crust6.grid(row=7, column=2, sticky=NW)
        self.bttn_order.grid(row=16, column=0, sticky=NW)
        self.output.grid(row=20, column=0, columnspan=3)
        self.output.config(width=40)

        self.pep = BooleanVar()
        self.create_cb(self.pep, "Pepperoni",10,0)
        self.mushroom = BooleanVar()
        self.create_cb(self.mushroom, "Mushroom", 10, 1)
        self.chicken = BooleanVar()
        self.create_cb(self.chicken, "Chicken", 10, 2)
        self.pineapple = BooleanVar()
        self.create_cb(self.pineapple, "Pineapple", 11, 0)
        self.sausage = BooleanVar()
        self.create_cb(self.sausage, "Sausage", 11, 1)
        self.Jalapeno = BooleanVar()
        self.create_cb(self.Jalapeno, "Jalapeno", 11, 2)
        self.greenpeppers = BooleanVar()
        self.create_cb(self.greenpeppers, "Green peppers", 12, 0)
        self.buffalochicken = BooleanVar()
        self.create_cb(self.buffalochicken, "Buffalochicken", 12, 1)
        self.olives = BooleanVar()
        self.create_cb(self.olives, "Olives", 12, 2)
        self.greenolives = BooleanVar()
        self.create_cb(self.greenolives, "Green Olives", 13, 0)
        self.ham = BooleanVar()
        self.create_cb(self.ham, "Ham", 13, 1)
        self.broccoli = BooleanVar()
        self.create_cb(self.broccoli, "Brocoli", 13, 2)
        self.excheese = BooleanVar()
        self.create_cb(self.excheese, "Extra Cheese", 14, 0)
        self.spinach = BooleanVar()
        self.create_cb(self.spinach, "Spinach", 14, 1)
        self.anchovies = BooleanVar()
        self.create_cb(self.anchovies, "Anchovies", 14, 2)
        self.cherrypeppers = BooleanVar()
        self.create_cb(self.cherrypeppers, "Cherry peppers", 15, 0)
        self.pesto = BooleanVar()
        self.create_cb(self.pesto, "Pesto", 15, 1)
        self.bacon = BooleanVar()
        self.create_cb(self.bacon, "Bacon", 15, 2)

    def order(self):
        order_size = self.size.get()

        order_crust = self.crust.get()
        toppings = []
        if self.pep.get():
            toppings.append("Pepperoni")
        if self.sausage.get():
            toppings.append("Sausage")
        if self.ham.get():
            toppings.append("Ham")
        if self.broccoli.get():
            toppings.append("Broccoli")
        if self.pesto.get():
            toppings.append("Pesto")
        if self.olives.get():
            toppings.append("Black Olives")
        if self.spinach.get():
            toppings.append("Spinach")
        if self.anchovies.get():
            toppings.append("Anchovies")
        if self.chicken.get():
            toppings.append("Chicken")
        if self.greenpeppers.get():
            toppings.append("Green Peppers")
        if self.excheese.get():
            toppings.append("Extra Cheese")
        if self.cherrypeppers.get():
            toppings.append("Cherry Peppers")
        if self.pineapple.get():
            toppings.append("Pineapple")
        if self.greenolives.get():
            toppings.append("Green Olives")
        if self.bacon.get():
            toppings.append("Bacon")

        message = f"Order Size: {order_size.capitalize()}, Order Crust: {order_crust.capitalize()}\n"
        for i in range(len(toppings)):
            message += toppings[i] + "\n"

        self.output.delete(0.0, END)
        self.output.insert(0.0, message)



    def create_cb(self, var, top, r, c):
        Checkbutton(self,
                    variable=var,
                    text=top,
                    ).grid(row=r, column=c, sticky=W)



def main():
    root = Tk()
    root.title("Text Boxes")
    root.geometry("300x600")
    root.attributes("-fullscreen", False)
    app = App(root)

    root.mainloop()

main()

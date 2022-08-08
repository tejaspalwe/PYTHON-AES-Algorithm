# Gui Main Panel
import login_page as lp  # Login page
import gui_demo as gd  # Registration Page
from tkinter import *  # Library Tkinter

main_root = Tk()
main_root.geometry("500x500");
main_root.configure(bg="#DBF4EC")
main_root.title("main_panel");
fontStyle = "Consolas 16 bold"
l1 = Label(main_root, text="Veermata Jijabai Technological Institute", font="Consolas 24 bold",
           bg="#DBF4EC")
l1.grid(row=0, column=2, padx=10, pady=10)

btn1 = Button(main_root, text="Registation Form", font=fontStyle,
              bg="#040D84", fg="white", command=gd.Registration_form)
btn1.grid(rows=1, column=0, padx=10, pady=10)
btn2 = Button(main_root, text="Login Page", font=fontStyle,
              bg="#040D84", fg="white", command=lp.login_pop)
btn2.grid(rows=2, column=0, padx=10, pady=10)

btn3 = Button(main_root, text="Close", font=fontStyle,
              bg="red", fg="white", command=main_root.destroy)
btn3.grid(rows=3, column=0, padx=10, pady=10)

mainloop()

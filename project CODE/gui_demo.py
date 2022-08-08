from tkinter import *
from tkinter import font
from db_eg_demo import *
import random
#import login_page as lp
def Registration_form():
	root = Tk()
	root.geometry("500x500");root.configure(bg = "#DBF4EC")
	root.title("basic project");fontStyle = "Consolas 16 bold"
	'''
	1.Title 2.Registration 
	'''

	#------------Title------------------------------------------#
	l1 = Label(root, text = "Registration form", font = "Consolas 24 bold", 
		bg = "#DBF4EC")
	l1.grid(row= 0, column=1, padx=10, pady=10)
	#---------------submit data------------------------------------------------
	#global variable now
	var1 = "";var2 = "";var3 = ""
	def submit_data():
		var1 = e2.get();var2 = e3.get();var3 = e4.get()
		add_data_db(var1, var2, var3)
		e2.delete(0, 'end');e3.delete(0, 'end');e4.delete(0, 'end')	
	#---------------------login pop---------------------------------------------


	#------------Registration------------------------------------#
		#---Email id--------
	l2 = Label(root, text = "User Id: ", font = fontStyle,bg = "#DBF4EC" )
	l2.grid(row = 1, column =0, padx =10, pady =10)
	e2 = Entry(root, bg = "white", fg = "black", font = fontStyle)
	e2.grid(row = 1, column =1, padx = 10, pady = 10)
		#--phone number-----
	l3 = Label(root, text = "Mobile Number: +91- ", font = fontStyle,bg = "#DBF4EC" )
	l3.grid(row = 2, column =0, padx =10, pady =10)
	e3 = Entry(root, bg = "white", fg = "black", font = fontStyle)
	e3.grid(row = 2, column =1, padx = 10, pady = 10)

		#---password----
	l4 = Label(root, text = "Password: ", font = fontStyle,bg = "#DBF4EC")
	l4.grid(row = 3, column =0, padx =10, pady =10)
	e4 = Entry(root, bg = "white", fg = "black", font = fontStyle)
	e4.grid(row = 3, column =1, padx = 10, pady = 10)

		#----submit button----
	btn1 = Button(root, text = "Submit Data", font = fontStyle, bg = "#040D84",
	 fg = "white", command = submit_data)
	btn1.grid(row= 4, column=1, padx =10, pady =10)

	btn2 = Button(root, text = "Close", font = fontStyle, bg = "red",
	 fg = "white", command = root.destroy)
	btn2.grid(row= 5, column=1, padx =10, pady =10)	

	#*****************Mainloop***************
	root.mainloop()

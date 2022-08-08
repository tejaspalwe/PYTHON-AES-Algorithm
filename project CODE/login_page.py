#login page
from tkinter import *
import random
import check_db
fontStyle = "Consolas 16 bold"
email_check = ""
import decrypt_panel as dp
def login_pop():
	#otp generations
	def generate_otp():
		global email_check
		var1 = "";var2= ""
		var1 = te2.get(); var2 = te3.get()
		email_check =te2.get()
		te2.delete(0, 'end');te3.delete(0, 'end')
		check_db.check_db_data(var1, var2)
	#1st verifications
	def first_verif():
		#email; pass+otp; message
		var1 = "";var2 = ""
		var1 = te5.get();var2 = te6.get()
		te5.delete(0, 'end');te6.delete(0, 'end')
		check_db.first_verif_data(var1, var2, email_check)
		#update_aes_check(email_check,var1,var2)

	w = Tk()
	w.title("Login Page");w.geometry("500x500");w.configure(bg = "#DBF4EC")
	tl1 = Label(w, text = "Login Page", font = "Consolas 24 bold", 
	bg = "#DBF4EC");tl1.grid(row= 0, column=1, padx=10, pady=10)
	#-----login email 
	#---Email id--------
	tl2 = Label(w, text = "User Id: ", font = fontStyle,bg = "#DBF4EC" )
	tl2.grid(row = 1, column =0, padx =10, pady =10)
	te2 = Entry(w, bg = "white", fg = "black", font = fontStyle)
	te2.grid(row = 1, column =1, padx = 10, pady = 10)
	tl3 = Label(w, text = "Mobile Number: +91- ", font = fontStyle,bg = "#DBF4EC" )
	tl3.grid(row = 2, column =0, padx =10, pady =10)
	te3 = Entry(w, bg = "white", fg = "black", font = fontStyle)
	te3.grid(row = 2, column =1, padx = 10, pady = 10)
	tbtn1 = Button(w, text = "Generate OTP",  font = fontStyle,
	 bg = "#040D84", fg = "white",command =generate_otp)
	tbtn1.grid(rows = 3, column = 1,padx =10, pady =10)
	tl5 = Label(w, text = "Password + OTP: ", font = fontStyle,bg = "#DBF4EC" )
	tl5.grid(row = 7, column =0, padx =10, pady =10)
	te5 = Entry(w, bg = "white", fg = "black", font = fontStyle)
	te5.grid(row = 7, column =1, padx = 10, pady = 10)
	tl6 = Label(w, text = "Message:", font = fontStyle,bg = "#DBF4EC" )
	tl6.grid(row = 8, column =0, padx =10, pady =10)
	te6 = Entry(w, bg = "white", fg = "black", font = fontStyle)
	te6.grid(row = 8, column =1, padx = 10, pady = 10)
	
	

	tbtn2 = Button(w, text = "Submit Details",   font = fontStyle,
	 bg = "#040D84", fg = "white",command = first_verif)
	tbtn2.grid(rows = 9, column = 1,padx =10, pady =10)
	tbtn2 = Button(w, text = "Crypto Check",   font = fontStyle,
	 bg = "#040D84", fg = "white",command = dp.decrypt_data)
	tbtn2.grid(rows = 10, column = 1,padx =10, pady =10)

	tbtn3 = Button(w, text = "Close",   font = fontStyle,
	 bg = "red", fg = "white",command = w.destroy)
	tbtn3.grid(rows = 12, column = 1,padx =10, pady =10)
	w.mainloop()

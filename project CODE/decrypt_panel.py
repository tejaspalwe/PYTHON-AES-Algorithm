#decrypt_panel
from tkinter import *
import check_db as db
from Crypto.Cipher import AES
fontStyle = "Consolas 16 bold"
def decrypt_data():
	def send_crypto_data():
		var1 = "";var2="";
		var1 = e2.get(); var2 = e3.get()
		db.dc(var1,var2)

	w = Tk()
	w.title("Decrypter Message");w.geometry("500x500");w.configure(bg = "#DBF4EC")
	tl1 = Label(w, text = "Decrypter", font = "Consolas 24 bold", 
	bg = "#DBF4EC");tl1.grid(row= 0, column=1, padx=10, pady=10)
	l2 = Label(w, text = "Password + OTP: ", font = fontStyle,bg = "#DBF4EC" )
	l2.grid(row = 1, column =0, padx =10, pady =10)
	e2 = Entry(w, bg = "white", fg = "black", font = fontStyle)
	e2.grid(row = 1, column =1, padx = 10, pady = 10)

	l3 = Label(w, text = "Crypto OTP: ", font = fontStyle,bg = "#DBF4EC" )
	l3.grid(row = 2, column =0, padx =10, pady =10)
	e3 = Entry(w, bg = "white", fg = "black", font = fontStyle)
	e3.grid(row = 2, column =1, padx = 10, pady = 10)
	tbtn3 = Button(w, text = "Check Message",   font = fontStyle,
	 bg = "#040D84", fg = "white",command = send_crypto_data)
	tbtn3.grid(rows = 5, column = 1,padx =10, pady =10)

	tbtn3 = Button(w, text = "Close",   font = fontStyle,
	 bg = "red", fg = "white",command = w.destroy)
	tbtn3.grid(rows = 5, column = 1,padx =10, pady =10)
	w.mainloop()

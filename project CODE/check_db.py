#check db
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("test_login_demo.db")
import otp_generation
import cryp_tejas
import send_data_templates as sdt
from Crypto.Cipher import AES
def check_db_data(email, mob):
	conn = sqlite3.connect("test_login_demo.db")
	command = "select * from login_demo_01 where email_id = ?"
	result = conn.execute(command, (email,))
	for i in result:
		email_id,mobile_number,password,otp,message,ciphertext,nonce,tag = i
	otp = otp_generation.generate_otp()
	new_otp = password+str(otp)
	sdt.send_otp(otp, email, mobile_number)
	print(new_otp) #needs to send to mobile
	command = f"""update login_demo_01 set otp = ?
	where email_id = ?"""
	conn.execute(command, (new_otp, email))
	conn.commit()
	conn.close()
	#1st verification
def first_verif_data(checkotp, new_message, email):
	conn = sqlite3.connect("test_login_demo.db")
	command = "select * from login_demo_01 where email_id = ?"
	result = conn.execute(command, (email,))
	for i in result:
		email_id,mobile_number,password,otp,message,ciphertext,nonce,tag = i
		print(i)
		otp = str(otp)
	if checkotp==otp:
		#otp #key
		#cmdnew_message #message to be crypted
		crypto_data = cryp_tejas.tejas_cryp(otp, new_message)
		ciphertext, tag, nonce = crypto_data
		new_4_otp = str(ciphertext)
		new_4_otp = new_4_otp[4:8]
		sdt.send_otp(new_4_otp, email, mobile_number) #needs to send to the mobile and email
		command = f"""update login_demo_01 set ciphertext = ?, tag = ?, nonce = ?,
		message = ? where email_id = ?""" #new_4_otp must included
		conn.execute(command, (ciphertext, tag, nonce, new_4_otp, email))
		conn.commit()
		command = "select * from login_demo_01 where email_id = ?"
		result = conn.execute(command, (email,))
		for i in result:
			email_id,mobile_number,password,otp,message,ciphertext,nonce,tag = i
			print(i)
		conn.close()
def dc(password, crypto_otp):
	print(password, crypto_otp)
	conn = sqlite3.connect("test_login_demo.db")
	command = "select * from login_demo_01 where message = ?"
	result = conn.execute(command, (crypto_otp,))
	for i in result:
		email_id,mobile_number,password_not,otp,message,ciphertext,nonce,tag = i
	#decrypting part
	keys = bytes(password, 'utf-8')
	cipher = AES.new(keys, AES.MODE_EAX, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)
	try:
		cipher.verify(tag)
		plaintext = plaintext.decode("utf-8")
		data = f"The message is authentic and access granted: {plaintext}"
		messagebox.showinfo("showinfo", data)
	except ValueError:
		print("Key incorrect or message corrupted",plaintext)


	conn.close()

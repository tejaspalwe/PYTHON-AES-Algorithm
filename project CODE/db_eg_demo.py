#db code
import sqlite3
conn = sqlite3.connect("test_login_demo.db")

def add_data_db(var1, var2, var3):
#for phone number string format is acceptable
	print(var1)
	print(var2)
	print(var3)
	conn.execute("""INSERT INTO login_demo_01(email_id, 
		mobile_number ,password) values (?, ?, ?)""",
 	(var1 ,var2 ,var3))
	conn.commit()
	command = "select * from login_demo_01"
	result = conn.execute(command)
	for i in result:
		email_id, mobile_number, password, otp, message, ciphertext, nonce, tag= i
		print(f"1:{email_id}, 2:{mobile_number}, 3:{password}", )



#email_id, mobile_number, password, otp, message, ciphertext, nonce, tag
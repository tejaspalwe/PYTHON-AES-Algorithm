#data bases testing
import sqlite3
conn = sqlite3.connect("test_login_demo.db")


#------creation of table
# command = '''create table login_demo_01(email_id text, mobile_number text,
#  password text, otp int, message text, 
# ciphertext blob, nonce blob, tag blob)'''



#-----------------inserting the data
# conn.execute("""INSERT INTO testing_data_02(user_key, otp,
#  ciphertext, nonce, tag) 
# 	values (?, ?, ?, ?, ?)""",
#  (User_keys ,otp ,ciphertext ,nonce ,tag))
# conn.commit()

#----------------updatind the data

# command = """update company_detail email id = 'Embedded_system (Arduino)' 
# where id = 1"""
# conn.execute(command)
# conn.commit()
#

#---------------Reading the data
command = "select * from login_demo_01"
result = conn.execute(command)
print(result)
for i in result:
	print(i)


#conn.execute(command)
#print("table is created")
conn.close()

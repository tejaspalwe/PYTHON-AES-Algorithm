#crypting_tejas
from Crypto.Cipher import AES
def tejas_cryp(password, message):
	User_keys = bytes(password, 'utf-8')
	print(User_keys)
	message = bytes(message,'utf-8')
	print(message)
	#creation of cipher model
	cipher = AES.new(User_keys, AES.MODE_EAX)
	nonce = cipher.nonce
	ciphertext, tag = cipher.encrypt_and_digest(message)
	return ciphertext, tag, nonce

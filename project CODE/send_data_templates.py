#send_data_templates
import requests
def send_otp(otp, email, mobile):
	#send message using fast2sms
	url = "https://www.fast2sms.com/dev/bulk"
	payload = f"sender_id=CHKSMS&message=Your otp code is:\n{otp} &language=english&route=p&numbers={mobile}"
	headers = {
	'authorization': "qkJ0xXwWoM6Ecmd9puejagYsi82rDtIyQZPRfVFKzl4NLb13UBLrJ0ti8lhbugO4asZUAQwXv3xSTmP2",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
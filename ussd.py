#atmombasa/ussd.py
import os
from flask import Flask, request
app = Flask(__name__)

#endpoint
@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
	session_id = request.values.get('sessionId', None)
	service_code = request.values.get('serviceCode', None)
	phone_number = request.values.get('phoneNumber', None)
	text = request.values.get('text', 'default')
	if text == '':
		response = 'CON What would you want to check \n'
		response += '1. My Account \n'
		response += '2. My Phone Number'
	elif text == '1':
		response = 'CON Choose Account info you want to view \n'
		response += '1. Account Number \n'
		response += '2. Account Balance'
	elif text == '1*1':
		accountNumber = 'ACC1001'
		response = 'END Your Account Number is ' + accountNumber
	elif text == '1*2':
		balance = 'KES 100,000'
		response = 'END Your Balance is ' + balance
	elif text == '2':
		response = 'Your Phone Number is ' + phone_number
	else:
		response = 'CON Invalid Choice. Try Again'

	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.environ.get('PORT'))



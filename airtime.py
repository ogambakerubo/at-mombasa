# Import the Africa's Talking module here
import africastalking

#Define credentials here
username = "araga"
api_key = "e5ddd4898d13ee49b727a2db9903785c047c68678853352d3267dbe90007545b"

#Authenticate with the service
africastalking.initialize(username, api_key)

#Define the airtime service
airtime = africastalking.Airtime 

#Define user variables
phone_number = "+254712391022"
amount = "5"
currency_code = "KES"

#Send the airtime!
response = airtime.send(phone_number = phone_number, amount = amount, currency_code = currency_code)
print(response)
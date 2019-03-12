#Import the Africa's Talking SDK
import africastalking

#Set up your credentials
username = "sandbox"
api_key = "305b514505c98ee53df3f7d995a27b9adc228eaf6c1e1fbc504a4acd239331c3"

#Initialize the SDK
africastalking.initialize(username, api_key)

#Define the Payment service
payments = africastalking.Payment

#Set your product name
product_name = "araga"

#Set the phone number you want and set it to the international format
phone_number = "+254734727107"

#Set the 3 letter ISO currency code and checkout amount
currency_code = "KES"
amount = 100.0

#You can add in your own metadata which will be resent back to you
#For the final payment notification
metadata = {
    "agentId": "Araga1",
    "productId": "01"
}

#Time to send and we'll handle the rest
try:
    res = payments.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
    print(res)
except Exception as e:
    print(f"Houston we have a problem {e}")

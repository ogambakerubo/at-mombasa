#Import the AfricasTalking SDK into your app
import africastalking

#Create your credentials
username = "araga"
apikey = "e5ddd4898d13ee49b727a2db9903785c047c68678853352d3267dbe90007545b"

#Initialize the SDK
africastalking.initialize(username, apikey)

#Get the SMS service
sms = africastalking.SMS

#Define some options that we will use to send the SMS
recipients = ['+254734727107', '+254799593900']
message = 'Welcome to Araga'
#sender = 'ARAGA'

#Send the SMS
try:
    #Once this is done, that's it! We'll handle the rest
    response = sms.send(message, recipients)
    print(response)
except Exception as e:
    print(f"Houston, we have a problem {e}")
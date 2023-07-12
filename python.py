from twilio.rest import Client
accountSID = 'AC12d1dba0c29f20305f566b48f4a18042'
authToken  = 'e300358f80ccc1fbd0c49f70493ae2c4'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+13203730928'
myCellPhone = '+2347066279211'
message = twilioCli.messages.create(body='Mr. Banjo - Congratulations -your American is VISA Approved.', from_=myTwilioNumber, to=myCellPhone)
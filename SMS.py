import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC28f8cb1eb71bf506face3b7f10cc2f68"
auth_token = "8b4424fde1f1bfa4b3b378a2c31cd6d1"
client_SMS = Client(account_sid, auth_token)

message = client_SMS.messages \
                .create(
                     body="From CS5001 team 2： Your room temperature is too high， please turn on the AC！ ：）",
                     from_='+16464614250',
                     to='+14089211926'
                 )

#print(message.sid)

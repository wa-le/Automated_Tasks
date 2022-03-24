# check if some websites in a csv file are online or offline, notify me by email and sms

import requests
import pandas as pd
from datetime import datetime
import smtplib
from twilio.rest import Client

curr_time = datetime.now()

# for email sending
my_email = "email to handle sending of alert"
my_email_pass = "email-password-here"
recipient_email = "recipient email here"


# for text sending
my_number = '+0000000000'
receive_number = '+0000000000'

account_sid = 'grab this on twilio'
auth_token = 'grab this on twilio'
client = Client(account_sid, auth_token)


df = pd.read_csv("monitor_sites.csv")
for index, websites in df.iterrows():
    # print(index, use_in_req)
    name = websites["website_name"]
    try:
        response = requests.get(url=websites["website_url"])
        # print(response.status_code)
        print(f"{curr_time} -> {name} is UP")
    except:
        print(f"{curr_time} -> {name} is DOWN")

        the_msg = f"Subject:Site Alert\n\n{name} is DOWN"		# message body for email
        the_msg_text = f"\n{name} is DOWN"				# message body for sms
        with smtplib.SMTP("smtp.gmail.com", port=587) as new_connect:
            # secure the connection
            new_connect.starttls()
            new_connect.login(user=my_email, password=my_email_pass)
            new_connect.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=the_msg)
	    
	    # using twilio to send sms	
            message = client.messages.create(
                                                body=the_msg_text,
                                                from_=my_number,
                                                to=receive_number
            )

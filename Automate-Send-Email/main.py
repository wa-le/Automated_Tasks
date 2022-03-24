
import random
import datetime as dt
import pandas
import smtplib

TO_REPLACE = "[NAME]"

# using datetime module, get current month and day
now = dt.datetime.now()
day = now.month
month = now.month

# read csv file and save to dictionary
data = pandas.read_csv("birthdays.csv")
data_to_dict = data.to_dict(orient="records")

# loop through dictionary containing each row and if the day and month match the current date
# send a random letter to the birthday person's email and add the birthday person's name to the letter
for birth_day in data_to_dict:
    if birth_day["month"] == month and birth_day["day"] == day:
        the_name = birth_day["name"]
        the_email = birth_day["email"]

        # select random letter and replace [name] with name
        letters = ['letter_1', 'letter_2', 'letter_3']
        letter = random.choice(letters)
        with open(f"./letter_templates/{letter}.txt") as file:
            the_letter = file.read()
            final_letter = the_letter.replace(TO_REPLACE, the_name)

        # send the email
        my_email = "mainstopstore@gmail.com"
        my_email_pass = "upperECHELON03"
        # connect to "your" email server
        with smtplib.SMTP("smtp.gmail.com", port=587) as new_connect:
            # secure the connection
            new_connect.starttls()
            new_connect.login(user=my_email, password=my_email_pass)
            new_connect.sendmail(from_addr=my_email, to_addrs=the_email, msg=f"Subject:Happy Birthday\n\n{final_letter}")

# import some libraries

import random
import smtplib
import datetime as dt

my_email = "example123@hotmail.com"
password = "example123"

# specify to receive and motivational e-mail every monday

if dt.datetime.now().weekday() == 0:

    with open("data/day32_quotes.txt") as quotes:
        list_of_quotes = quotes.readlines()
        quote_of_today = random.choice(list_of_quotes)
        subject = quote_of_today.split("-")[1]
        message = quote_of_today.split("-")[0]

    with smtplib.SMTP("smtp.office365.com") as new_conn:
        new_conn.starttls()
        new_conn.login(user=my_email, password=password)
        new_conn.sendmail(from_addr=my_email, to_addrs=my_email,
                          msg= f"Subject:{subject}\n\n{message}")
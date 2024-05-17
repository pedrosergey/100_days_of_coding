# import some libraries

import random
import smtplib
import datetime as dt
import pandas as pd

# set the credentials to log in

my_email = "example123@hotmail.com"
password = "example123"

# read the csv file

df = pd.read_csv("data/day32_birthdays.csv")


# create the function to send the emails

def send_letter(birthday_index):
    letter_number = random.randint(1, 3)
    birthday_name = df.loc[birthday_index]["name"]

    with open(f"data/day32_letter-templates/letter_{letter_number}.txt") as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_name)

    with smtplib.SMTP("smtp.office365.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr=my_email, to_addrs=df.loc[birthday_index]["email"],
                      msg=f"Subject:Happy Birthday!:)\n\n{content}")


# create the condition and send the messages if is the actual date

today_day = dt.datetime.now().day
today_month = dt.datetime.now().month

for index, row in df.iterrows():
    birthday_day = row["day"]
    birthday_month = row["month"]

    if birthday_day == today_day and birthday_month == today_month:
        send_letter(index)

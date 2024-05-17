# import the necessary libraries
import datetime

import requests
import smtplib

# reference the APIs that we will use

ISS_url = "http://api.open-notify.org/iss-now.json"
sunrise_url = "https://api.sunrise-sunset.org/json"

# latitude and longitude of Tenerife

latitude_tnf = 28.291565
longitude_tnf = -16.629129

# set the email and the password

my_email = "example123@hotmail.com"
password = "example123"


# create a function to get the current time of sunrise and sunset

def get_sun_hours(latitude, longitude):
    response = requests.get(url=sunrise_url, params={"lat": latitude, "lng": longitude, "formatted": 0})
    response.raise_for_status()
    response_json = response.json()

    sunrise = int(response_json["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response_json["results"]["sunset"].split("T")[1].split(":")[0])

    return sunrise, sunset


def get_ISS_position():
    response = requests.get(url=ISS_url)
    response.raise_for_status()
    response_json = response.json()

    latitude = float(response_json["iss_position"]["latitude"])
    longitude = float(response_json["iss_position"]["longitude"])

    return latitude, longitude


def send_email():
    with smtplib.SMTP("smtp.office365.com") as new_conn:
        new_conn.starttls()
        new_conn.login(user=my_email, password=password)
        new_conn.sendmail(from_addr=my_email, to_addrs="grone.93@gmail.com",
                          msg="Subject: ISS visible\n\nLook to the sky! :)")


# create two functions to check if is dark and if the ISS is visible

def is_night():
    if current_hour <= tnf_sunrise or current_hour >= tnf_sunset:
        return True
    else:
        return False


def iss_visible():
    if (latitude_tnf - 5 <= latitude_iss <= latitude_tnf + 5) and (
            longitude_tnf - 5 <= longitude_iss <= longitude_tnf + 5):
        return True
    else:
        return False


current_hour = datetime.datetime.now().hour

tnf_sunrise, tnf_sunset = get_sun_hours(latitude=latitude_tnf, longitude=longitude_tnf)
latitude_iss, longitude_iss = get_ISS_position()

# send the email when the conditions are met

if is_night() and iss_visible():
    send_email()

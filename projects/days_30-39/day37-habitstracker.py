# import some libraries

import requests
import datetime

# make some constants

TOKEN = "testingtheapp"
USERNAME = "perro-sato"
GRAPH = "testing-limits"

# creating a user

pixela_endpoint = "https://pixe.la/v1/users"

params_create_user = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=params_create_user)
response.raise_for_status()

# create a graph

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

params_create_graph = {
    "id": GRAPH,
    "name": "Daily Running",
    "unit": "kilometers",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# posting something to a graph

posting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.datetime.now()
today_formated = today.strftime("%Y%m%d")

params_posting_pixel = {
    "date": today_formated,
    "quantity": "8.9",
}

response = requests.post(url=posting_endpoint, json=params_posting_pixel, headers=headers)
response.raise_for_status()

# putting something in a graph

putting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today_formated}"

params_putting_pixel = {
    "date": today_formated,
    "quantity": "18.9",
}

response = requests.put(url=putting_endpoint, json= params_putting_pixel, headers=headers)
response.raise_for_status()

# deleting something from a graph

response = requests.delete(url=putting_endpoint, headers=headers)
response.raise_for_status()

import requests
from datetime import datetime

USERNAME = "berkeztrk"
TOKEN = "ab12(7!5%1*b46nf=((hlg"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
post_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph0"
update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph0/20250224"

today = datetime.now()

pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_parameters = {
    "id": "graph0",
    "name": "Cloud Study Graph",
    "unit": "Hour",
    "type": "float",
    "color": "sora",
}

post_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

update_parameters = {
    "quantity": "2",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# creating user
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

#creating graph
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)
# #https://pixe.la/v1/users/berkeztrk/graphs/graph0.html

#post pixel
# response = requests.post(url=post_pixel_endpoint, json=post_parameters, headers=headers)
# print(response.text)

#update pixel
# response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
# print(response.text)

#delete pixel
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)

















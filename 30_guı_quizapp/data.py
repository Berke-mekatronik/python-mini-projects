import requests
import smtplib

parameters = {
    "amount": 10,
    "category": 23,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
# it will raise exception if there is an error
response.raise_for_status()
data = response.json()
question_data = data["results"]

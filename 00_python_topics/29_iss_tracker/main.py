import requests
from datetime import datetime

MY_LAT = 41.037363  # my latitude
MY_LONG = 28.875931 # my longitude

def is_iss_overhead():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()

    iss_latitude  = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status()

    data2 = response2.json()

    sunrise = data2["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset  = data2["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    print("Message has been send")
import requests
import datetime

GENDER    = "male"
WEIGHT_KG = 76
HEIGHT_CM = 180
AGE       = 26

APP_ID  = "225c7536"
API_KEY = "915eb34176fe81ccec2f7e7574eca601"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_ENDPOINT = "https://api.sheety.co/0d0cd3ee86da6e82551ecf6ed1a7beb3/myWorkoutsPythonApi/workouts"

exerciseInput = input("Tell me which exercises you did: ")
#print(exerciseInput)

headers = {
    "x-app-id":  APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exerciseInput,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=API_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
exercise_data = response.json()

print(exercise_data)
#example_data = {'exercises': [{'tag_id': 765, 'user_input': 'yoga', 'duration_min': 30, 'met': 3.3, 'nf_calories': 115.5, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/765_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/765_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 2180, 'name': 'yoga', 'description': None, 'benefits': None}]}

today_date = datetime.datetime.now()
today_date = today_date.strftime("%d/%m/%Y")

today_time = datetime.datetime.now()
current_time = today_time.strftime("%X")

for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_API_ENDPOINT, json=sheet_inputs)

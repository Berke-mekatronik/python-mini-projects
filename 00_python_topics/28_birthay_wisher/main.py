import pandas
import datetime as dt
import random
import smtplib

PASSWORD = "ensbcpvftfdghjmf"

now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

# birthdays_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        text = letter_file.read()
        text  = text.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # to secure connection
        connection.starttls()
        # to login
        connection.login(user="sender@gmail.com", password=PASSWORD)
        # send email
        connection.sendmail(from_addr="sender@gmail.com",
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{text}"
                            )


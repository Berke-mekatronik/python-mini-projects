import datetime as dt
import random
import smtplib

MY_EMAIL = "sender@gmail.com"
PASSWORD = "ensbcpvftfdghjmf"

# Using the datetime module to obtain the current day of the week
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if day_of_week == 0:
    # date_of_birth = dt.datetime(year=1998, month=12, day=9, hour=21)
    # print(date_of_birth)

    # Opening the quotes.txt file and obtain a list of quotes
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
    #print(name_list[0])

    # Using random module to pick a random quote from list of quotes
    random_quote = random.choice(quotes_list)
    print(random_quote)

    # By default smtplib.SMTP uses port 25. This used to be the standard SMTP port, but because of abuse in the past most servers
    # nowadays have blocked this port to external traffic. There are still some that do allow it; Hotmail, Live, etc. Port 25 is
    # still used for traffic between servers, but many providers have switched to using port 587 for external traffic. If in
    # doubt, search the internet for "smtp server settings" for your provider.
    #
    # Add a port number by changing your code to this:

    # Using smtplib to send the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # to secure connection
        connection.starttls()
        # to login
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # send email
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="receiver@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{random_quote}"
                            )

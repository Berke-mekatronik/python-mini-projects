import requests
import smtplib
from PIL.ImageChops import difference

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
FIRST_API_KEY = "HAELIB8B3CEZ7OTC"
SECOND_API_KEY = "6311896db5e9462ab8432d7ac889ae6e"

# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apikey": FIRST_API_KEY
# }
#
# response = requests.get(url=STOCK_ENDPOINT, params=parameters)
# response.raise_for_status()
# stock_data = response.json()["Time Series (Daily)"]

stock_data = {'2025-02-21': {'1. open': '353.4400', '2. high': '354.9800', '3. low': '334.4200', '4. close': '337.8000', '5. volume': '74058648'},
              '2025-02-20': {'1. open': '361.5100', '2. high': '362.3000', '3. low': '348.0000', '4. close': '354.4000', '5. volume': '45965354'},
              '2025-02-19': {'1. open': '354.0000', '2. high': '367.3400', '3. low': '353.6700', '4. close': '360.5600', '5. volume': '67094374'},
              '2025-02-18': {'1. open': '355.0100', '2. high': '359.1000', '3. low': '350.0200', '4. close': '354.1100', '5. volume': '51631702'},
              }

stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

before_yesterday_data = stock_data_list[1]
before_yesterday_closing_price = float(before_yesterday_data["4. close"])
print(before_yesterday_closing_price)

# pos_dif = float(yesterday_closing_price) - float(before_yesterday_closing_price)
# pos_dif = abs(pos_dif)
# print(pos_dif)

percentage = (100 * yesterday_closing_price) / before_yesterday_closing_price
percentage = 100 - percentage
print(percentage)

if percentage > 4:

    # parameters_2 = {
    #     "q": COMPANY_NAME,
    #     "from": "2025-01-23",
    #     "sortBy": "publishedAt",
    #     "apiKey": SECOND_API_KEY
    #
    # }

    # response = requests.get(url=NEWS_ENDPOINT, params=parameters_2)
    # response.raise_for_status()
    # news_data = response.json()
    # print(news_data)

    news_data = {
      'status': 'ok',
      'totalResults': 1042,
      'articles': [
        {
          'source': {
            'id': 'the-times-of-india',
            'name': 'The Times of India'
          },
          'author': 'PTI',
          'title': 'Piyush Goyal says Tesla welcome to invest, manufacture in India',
          'description': "Union Minister Piyush Goyal welcomes Tesla and other global companies to invest and manufacture in India. He emphasized mutual benefits and highlighted the government's commitment to reducing pollution through electric vehicles. Addressing US-India relations,…",
          'url': 'https://economictimes.indiatimes.com/industry/renewables/piyush-goyal-says-tesla-welcome-to-invest-manufacture-in-india/articleshow/118486584.cms',
          'urlToImage': 'https://img.etimg.com/thumb/msid-118486605,width-1200,height-630,imgsize-86226,overlay-economictimes/articleshow.jpg',
          'publishedAt': '2025-02-22T17:45:51Z',
          'content': 'Mumbai: India welcomes Tesla and also all the other global companies which want to invest and manufacture in the country, Union Minister Piyush Goyal said on Saturday. Replying to a question on Elon … [+2790 chars]'
        },
        {
          'source': {
            'id': None,
            'name': 'Atomix'
          },
          'author': 'Samuel Yépez',
          'title': 'Meta está trabajando en androides',
          'description': 'La compañía dueña de Facebook, Instagram y Threads, Meta, está trabajando en tecnologías de robots autónomos que sean capaces de cuidar el hogar. La iniciativa se centra en la creación de inteligencia artificial avanzada, sensores y software que permitirán a …',
          'url': 'https://atomix.vg/meta-esta-trabajando-en-androides/',
          'urlToImage': 'https://cdn.atomix.vg/wp-content/uploads/2025/02/Roboto.png',
          'publishedAt': '2025-02-22T15:30:39Z',
          'content': 'La compañía dueña de Facebook, Instagram y Threads, Meta, está trabajando en tecnologías de robots autónomos que sean capaces de cuidar el hogar. La iniciativa se centra en la creación de inteligenci… [+1290 chars]'
        },
        {
          'source': {
            'id': None,
            'name': 'Securityaffairs.com'
          },
          'author': 'Pierluigi Paganini',
          'title': 'Apple removes iCloud encryption in UK following backdoor demand',
          'description': 'Apple removed iCloud’s Advanced Data Protection in the UK after the government requested encryption backdoor access. Apple ends iCloud end-to-end encryption in the United Kingdom following the government’s request for encryption backdoor access. Advanced Data…',
          'url': 'https://securityaffairs.com/174500/security/apple-removes-icloud-encryption-in-uk.html',
          'urlToImage': 'https://securityaffairs.com/wp-content/uploads/2025/02/image-38.png',
          'publishedAt': '2025-02-22T11:50:56Z',
          'content': 'Lazarus APT stole $1.5B from Bybit, it is the largest cryptocurrency heist ever\r\n\xa0|\xa0Apple removes iCloud encryption in UK following backdoor demand\r\n\xa0|\xa0B1acks Stash released 1 Million credit cards\r\n\xa0… [+141406 chars]'
        },
        {
          'source': {
            'id': None,
            'name': 'Livemint'
          },
          'author': 'Livemint',
          'title': "Tesla price in India: How much will Elon Musk's cheapest EV cost even with lower tariffs? Check details",
          'description': 'A CLSA report has highlighted that with a reduced tariff rate of 15-20 per cent, Tesla price in India will be more expensive than its domestic competitors like Maruti Suzuki. The company will need to open a manufacturing unit in India to keep up with competit…',
          'url': 'https://www.livemint.com/companies/news/tesla-price-in-india-how-much-will-elon-musk-cheapest-ev-cost-even-with-lower-tariffs-check-details-11740221738212.html',
          'urlToImage': 'https://www.livemint.com/lm-img/img/2025/02/22/1600x900/im-91133283_1739358749230_1740221954476.jpg',
          'publishedAt': '2025-02-22T11:11:37Z',
          'content': 'Elon Musks Tesla is gearing up for its entry in India, but buying a car from the EV maker may not be as easy as you thought even with reduced tariffs.\r\nAccording to a report by ANI quoting global cap… [+2232 chars]'
        },
                    ]
    }

    articles = news_data['articles']
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    print(formatted_articles)

    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     # to secure connection
    #     connection.starttls()
    #     # to login
    #     connection.login(user="sender@gmail.com", password="random password")
    #     # send email
    #     for article in formatted_articles:
        #     connection.sendmail(from_addr="sender@gmail.com",
        #                         to_addrs="sender@gmail.com",
        #                         msg=article
        #                         )




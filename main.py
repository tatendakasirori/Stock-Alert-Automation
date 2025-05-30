import os 
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from stock_change import Stock_change
from twilio.rest import Client
load_dotenv()

STOCK_KEY = os.environ["STOCK_KEY"]
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

### Monitoring changes to TESLA stock

today = datetime.now().date()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))

stock_params = {
"function": "TIME_SERIES_DAILY",
"symbol":STOCK,
"outputsize":"compact",
"apikey": STOCK_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
stock_response.raise_for_status()


close_price_yesterday = float(stock_response.json()["Time Series (Daily)"][yesterday]['4. close'])
close_price_two_days_ago = float(stock_response.json()["Time Series (Daily)"][day_before_yesterday]['4. close'])

stock_change = Stock_change(close_price_yesterday,close_price_two_days_ago)

if stock_change.abs_percentage > 5:

    ### Getting related articles 

    NEWS_KEY = os.environ["NEWS_KEY"]
    parameters = {
        "q": COMPANY_NAME,
        "from": day_before_yesterday,
        "to":yesterday,
        "apiKey": NEWS_KEY
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything",params=parameters)
    news_response.raise_for_status()
    print(news_response.status_code)
    articles = news_response.json()["articles"][:3]

    # Sending messages alerts via twilio
    for article in articles:
        message_body = f"{STOCK}: {stock_change.percentage_change}\nHeadline: {article['title']}\nBrief: {article['description']}"
        account_sid = os.environ["TWILIO_ACC_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_= os.environ["WHATS_APP_FROM_NUM"],
        body=message_body,
        to=os.environ["WHATS_APP_TO_NUM"]
        )
        print(message.status)






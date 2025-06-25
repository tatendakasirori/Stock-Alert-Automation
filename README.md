# Stock Alert Automation

A Python script that monitors significant daily stock price changes and sends real-time WhatsApp alerts with related news articles.

## Project Overview

This tool tracks daily closing prices of a specified stock (default: Tesla Inc.) using the Alpha Vantage API. If the stock price changes by more than 5% compared to the previous day, it fetches the latest relevant news using NewsAPI and sends summarized alerts via Twilio WhatsApp messaging.

## Features

- Fetches daily stock prices and calculates percentage change.
- Detects significant stock movements (threshold set at 5%).
- Retrieves top 3 recent news articles related to the company.
- Sends WhatsApp alerts containing stock change and news headlines via Twilio.
- Uses environment variables to securely manage API credentials.

## Setup & Installation

1. Clone the repository:
- git clone https://github.com/yourusername/stock-alert-automation.git
- cd stock-alert-automation
2. Install dependencies:
- pip install -r requirements.txt
3. Create a .env file in the project root and add your API keys and credentials:
- STOCK_KEY=your_alpha_vantage_api_key
- NEWS_KEY=your_newsapi_key
- TWILIO_ACC_SID=your_twilio_account_sid
- TWILIO_AUTH_TOKEN=your_twilio_auth_token
- WHATS_APP_FROM_NUM=your_twilio_whatsapp_number
- WHATS_APP_TO_NUM=your_destination_whatsapp_number

## Usage
- Adjust the stock symbol and company name in the script as needed.
- For automation, schedule the script with cron (Linux/macOS) or Task Scheduler (Windows) to run daily.

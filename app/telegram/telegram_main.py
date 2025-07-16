import requests
from datetime import datetime
import json

with open ('app/telegram/.telegram_settings', 'r') as fr:
    telegram_settings = json.load(fr)

def send_telegram_message(jobtype: str, message: str) -> dict:
    """
    Function to send a message to a Telegram bot.
    """

    bot_token = telegram_settings[jobtype]["bot_token"]
    chat_id = telegram_settings[jobtype]["chat_id"] 
    if not bot_token or not chat_id:
        return {
            "statusCode": "ERROR",
            "statusMessage": "Bot token or chat ID is missing.",
            "EndTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"Job Type: {jobtype}\nMessage: {message}"
    }
    response = requests.post(url, json=payload, timeout=10)
    if response.status_code != 200:
        return {
            "statusCode": "ERROR",
            "statusMessage": f"Failed to send message: {response.text}",
            "EndTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    else:
        return {
            "statusCode": "OK",
            "statusMessage": f"Send to telegram ok: {response.text}",
            "EndTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

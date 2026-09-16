import requests
import time

TOKEN = "8902899866:AAHjN9Jux-2_zNvJGDhJtUI3NVwukVTLG1g"
CHAT_ID = "1052745246"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

send_message("✅ PeDocUCAAlertBot is running!")

while True:
    time.sleep(60)

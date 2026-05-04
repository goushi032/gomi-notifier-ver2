import requests
from config import LINE_TOKEN, USER_ID


def send_line(message):
    url = "https://api.line.me/v2/bot/message/push"
    
    token = os.environ["LINE_TOKEN"]
    user_id = os.enviorn["USER_ID"]

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    res = requests.post(url, headers=headers, json=data)
    print(res.status_code, res.text)
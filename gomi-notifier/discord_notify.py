import requests


WEBHOOK_URL = "https://discord.com/api/webhooks/1499661998177124375/d9Y5wGW6DLXuRHDmligFDUaefIbDvJwglGrANV-wF__C2kpwORMrwe7SU83Kr25kzLLG"

def send_discord(message):
    data = {
        "content": message
    }

    requests.post(WEBHOOK_URL, json=data)



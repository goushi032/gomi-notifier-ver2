import requests 
from config import URL

def get_schdule_html():
    res = requests.get(URL)
    res.encoding = res.apparent_encoding
    return res.text
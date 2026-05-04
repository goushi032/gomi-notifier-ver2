from bs4 import BeautifulSoup
import datetime

def parse_schedule(html):
    soup = BeautifulSoup(html, "html.parser") #htmlを解析

    header_row = soup.find("tr")
    headers = [th.get_text(strip=True) for th in header_row.find_all(["th", "td"])]

    rows = soup.find_all("tr")
        
    for row in rows:
        text = row.get_text()

        if "南太田1～4丁目" in text:
            cols = [th.get_text(strip=True) for th in row.find_all(["th", "td"])]

            data = dict(zip(headers, cols))

            return data

    return None


def get_tomorrow_gomi(schedule):
    jp_week = ["月曜日","火曜日","水曜日","木曜日","金曜日","土曜日","日曜日"]

    tomorrow = datetime.date.today() + datetime.timedelta(days=1) #今日の日付を西暦で表す。
    weekday = jp_week[tomorrow.weekday()] #その日が何曜日か数字で返す

    return schedule.get(weekday)
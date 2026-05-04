from scraper import get_schdule_html
from parser import parse_schedule, get_tomorrow_gomi
from line_bot import send_line

def main():
    html = get_schdule_html()

    schedule = parse_schedule(html)

    if schedule is None:
        send_line("ゴミ情報の取得に失敗しました")
        return

    gomi = get_tomorrow_gomi(schedule)

    

    if gomi:
        message = f"明日のゴミは「{gomi}」です"
    else:
        message = "明日のゴミ情報はありません"

    send_line(message)




    

if __name__ =="__main__":
    main()
        
import requests
from bs4 import BeautifulSoup
import vk_api
import time

token = "" # ваш токен
url = "https://store.steampowered.com/search/?maxprice=free&specials=1&ndl=1" # ссылка на страницу для парсинга
"""
https://store.steampowered.com/search/?maxprice=free&specials=1&ndl=1
"""

vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
vk = vk_session.get_api()


def sender(id, text):  # send function
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})  # just remember


while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            games = soup.find("div", {"id": "search_resultsRows"}).find_all("a")
            File = open("listofgames.txt", "r")
            stripofgames = str(File.readline())
            listofgames = ""
            for game in games:
                log = ""
                name = game.find("span", {"class": "title"}).text.strip()
                if not (str(name) in stripofgames):
                    href = game['href']
                    log += f"Name: {name}" + "\n"
                    log += f"Link: {href}" + "\n"
                    sender(2, log) # вместо 2 указать номер вашей беседы
                    print(log)
                listofgames += name + "|"
            File.close()
            File = open("listofgames.txt", "w")

            File.write(listofgames)
            File.close()
            time.sleep(3600) # раз во сколько минут проверять
    except:
        time.sleep(3600)  # раз во сколько минут проверять
        continue

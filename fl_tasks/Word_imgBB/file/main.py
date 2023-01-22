from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup
import time
from google_sheet import gs
from config_tg import api_id, api_hash, chat_name

class NameChannel: # Можно ли получить имя
    def __init__(self, link):
        self.link = link

    def response(self):
        response_chanell = requests.get(self.link)
        soup = BeautifulSoup(response_chanell.text, 'html.parser')
        title = soup.find('div', 'tgme_page_title')
        return title.text


client = TelegramClient(session='session_name', api_id=api_id, api_hash=api_hash)
client.start()


@client.on(events.NewMessage(chats=(chat_name)))
async def function(event):
    message_date = event.date  # 1 COLUMN DATE
    print(message_date)
    message_text = event.message.text
    print(message_text)
    print('-------')
    name_channel = message_text.split('**')[1]  # ссылка для паблика
    print(name_channel)
    link_chanell = 'https://t.me/+' + name_channel  # 3 column ССЫЛКА НА ПАБЛИК
    print(link_chanell)  # работает

    link_chanell_class = NameChannel(str(link_chanell))
    time.sleep(1)
    try:
        t = link_chanell_class.response() # название паблика
        link_pablic = (message_text.split('**')[2]).split('\n')[0] # ссылка на пост
        number = gs.read_file()
        print(message_text.split('**'))
        print(link_pablic)
        data = [str(message_date), str(t), str(link_chanell), str(link_pablic)]
        gs.write_file(data=data, sheet_number=int(number)+1)


    except Exception as ex:
        link_pablic = (message_text.split('**')[2]).split('\n')[0] # ссыклка на пост
        gs.read_file()
        number = gs.read_file()
        print(link_pablic)
        data = [[str(message_date), 'none', str(link_chanell), str(link_pablic)]]
        gs.write_file(data=data, sheet_number=int(number) + 1)


if __name__ == '__main__':
    client.run_until_disconnected()
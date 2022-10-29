import requests
from bot_token import token
from searching_script import fill_matched_sentences, create_result_message
ok_codes = 200, 201, 202, 203, 204

user = {"username": "Ludvig", "level": 1}

class Bot:
    root_url = "https://api.telegram.org/bot"

    def __init__(self, token=None):
        self.token = token

    def get_updates(self):
        url = f"{self.root_url}{self.token}/getUpdates"
        res = requests.get(url)

        if res.status_code in ok_codes:
            updates = res.json()
            return updates

    def send_message(self, chat_id, message):
        url = f"{self.root_url}{self.token}/sendMessage"
        res = requests.post(url, data={"chat_id": chat_id, "text": message})
        if res.status_code in ok_codes:
            return True
        else:
            print(f"Request failed with status_code {res.status_code}")
            return False

    # processing the incoming message and issuing a response that will be sent to the user
    def process_message(self, message: str) -> str:
        # matched_sentences = fill_matched_sentences(message=message, user=user, sentences=sentences)
        matched_sentences = fill_matched_sentences(message, user)
        message = create_result_message(matched_sentences)
        return message

    def poolling(self):
        last_message_id = 0

        while True:
            updates = self.get_updates()
            last_message = updates["result"][-1]
            message_id = last_message["message"]["message_id"]

            last_message_text = last_message["message"]["text"]
            chat_id = last_message["message"]["chat"]["id"]

            if message_id > last_message_id:
                message_to_user = self.process_message(last_message_text)
                self.send_message(chat_id, message_to_user)
                last_message_id = message_id


bot = Bot(token)
bot.poolling()

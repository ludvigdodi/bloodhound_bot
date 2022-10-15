import requests
from bot_token import token

ok_codes = 200, 201, 202, 203, 204

user = {"username": "Ludvig", "level": 1}


sentences = [
    {"text": "When my time comes \n Forget the wrong that I’ve done.", "level": 1},
    {"text": "In a hole in the ground there lived a hobbit.", "level": 2},
    {
        "text": "The sky the port was the color of television, tuned to a dead channel.",
        "level": 1,
    },
    {"text": "I love the smell of napalm in the morning.", "level": 0},
    {
        "text": "The man in black fled across the desert, and the gunslinger followed.",
        "level": 0,
    },
    {"text": "The Consul watched as Kassad raised the death wand.", "level": 1},
    {"text": "If you want to make enemies, try to change something.", "level": 2},
    {
        "text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore",
        "level": 1,
    },
    {
        "text": "I learned very early the difference between knowing the name of something and knowing something.",
        "level": 2,
    },
]


def fill_matched_sentences(message, user, sentences) -> list:
    matched_sentences = []
    for sentence in sentences:
        user_lvl = user.get("level")
        sentences_lvl = sentence.get("level")
        sentences_txt = sentence.get("text")
        if sentences_lvl == user_lvl:
            if message in sentences_txt:
                matched_sentences.append(sentences_txt)
    return matched_sentences


def create_result_message(matched_sentences: list) -> str:
    result_message = ""
    if not matched_sentences:
        result_message = "Sorry, not found sentences for your request"
    if len(matched_sentences) == 1:
        result_message = matched_sentences[0]
    if len(matched_sentences) > 1:
        for x in matched_sentences:
            result_message += x + "\n...\n"
    return result_message


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

    def process_message(self, message: str) -> str:
        """обрабтывает входящее сообщение и выдает ответ, который будет отправлен юзеру"""
        matched_sentences = fill_matched_sentences(
            message=message, user=user, sentences=sentences
        )
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

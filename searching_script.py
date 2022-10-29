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


def fill_matched_sentences(message, user, sentences=sentences) -> list:
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


import pytest
import sys
sys.path.append("..")

from searching_script import fill_matched_sentences

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


def test_fill_matched_sentences():
    expected_result = ["The Consul watched as Kassad raised the death wand."]
    input_message = "watched"
    user_level = 1
    assert (
        fill_matched_sentences(input_message, user, sentences) == expected_result
    )


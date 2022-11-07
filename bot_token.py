from os import environ as env

# token = "5488524499:AAG1Jsp4ESZ_MRpPVLbqeOM12WEhrj-MXIg"

token = env.get("TOKEN")
assert token != None
run localy:
python bloodhound_bot.py


run in container:

docker build -t bot:v1 .
or
docker build -t bot:v1 -f custom-dockerfile .


docker run -e TOKEN=your-token bot:v1
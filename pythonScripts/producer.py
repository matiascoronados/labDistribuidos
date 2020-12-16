from kafka import KafkaProducer
from json import dumps
import praw
from pretty import pprint


reddit = praw.Reddit(client_id="MBLqAl5yrZENtA",
                     client_secret="gqpmFImIXEOkozg3u7_WgrG9iRUi-w",
                     password="canito123",
                     user_agent="redditcanitobotapp by u/redditcanitorealbot",
                     username="redditcanitorealbot")

print(reddit.user.me())

subreddit = reddit.subreddit("memes")

top = subreddit.hot(limit=1)

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'), 
   bootstrap_servers=["34.68.42.248:9091"])

for submission in top:
    #pprint(dir(submission))
    pprint(submission.over_18)
    producer.send('Temas', value={"title":submission.title},partition=2)
producer.flush()



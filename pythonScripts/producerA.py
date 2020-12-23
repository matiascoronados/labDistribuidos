from kafka import KafkaProducer
from json import dumps
import praw
from pretty import pprint
from langdetect import detect
from random import randrange


reddit = praw.Reddit(client_id="MBLqAl5yrZENtA",
                     client_secret="gqpmFImIXEOkozg3u7_WgrG9iRUi-w",
                     password="canito123",
                     user_agent="redditcanitobotapp by u/redditcanitorealbot",
                     username="redditcanitorealbot")

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'), 
   bootstrap_servers=["34.68.42.248:9091"])

comments = reddit.subreddit("all").stream.comments()

for comment in comments:
    #pprint(dir(submission))
    #pprint(dir(comment))
    submission = comment.submission
    
    if submission.is_video == False and detect(submission.title) == 'en':
        if comment.over_18 == False:

            print('comment')            
            producer.send('Temas', 
            value={
                # Info de Comentarios
                "commentId" : str(comment.id), 
                "commentAuthor" : str(comment.author),
                "commentBody" : str(comment.body),
                # Info de Submissions(Posts)
                "postId" : str(submission.id),
                "postAuthor" : str(submission.author) ,
                "postTitle" : str(submission.title),
                "postScore" : str(submission.score),
                "postLink" : str(submission.shortlink),
                "postNumComments" : str(len(submission.comments)),
                # Info de Subreddit(Topico o tema)
                "subredditTitle" : str(comment.subreddit.title)     
            },
            partition=randrange(3))
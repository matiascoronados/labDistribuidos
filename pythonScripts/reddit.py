import praw

reddit = praw.Reddit(client_id="MBLqAl5yrZENtA",
                     client_secret="gqpmFImIXEOkozg3u7_WgrG9iRUi-w",
                     password="canito123",
                     user_agent="redditcanitobotapp by u/redditcanitorealbot",
                     username="redditcanitorealbot")

print(reddit.user.me())

subreddit = reddit.subreddit("memes")

top = subreddit.hot(limit=10)

for submission in top:
    print(submission.title)




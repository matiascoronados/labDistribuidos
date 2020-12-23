from kafka import KafkaConsumer
from json import loads
import pymongo
from pymongo import MongoClient
from pymongo import *
from langdetect import detect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import nltk

def countstops(text):
    text.lower()
    texto = text.split(" ")
    count_stopwords = 0
    for i in texto:
        if(i in nltk_stopwords):
            count_stopwords+=1
    text_without_stopword = [word for word in text.split() if word.lower() not in nltk_stopwords]
    final = ' '.join(text_without_stopword)
    #print(final)
    return count_stopwords, final

def upperLetters(comment):
#    nltk.download('stopwords')
    upper = 0
    lower = 0
    vowel = 0
    consonant = 0
    stops = 0
    vocals= ["a","e","i","o","u"]

    words =[]

    #print(comment["commentBody"])
    for letter in comment:
        if(letter.isupper()):
            upper+=1
        elif(letter.islower()):
            lower+=1
        if(letter in vocals):
            vowel+=1
        else:
            consonant+=1

    count_stopwords, text_without_stopword = countstops(comment)
    words = comment.split(" ")
    count_words = len(words)
    return upper,lower,vowel,consonant,stops, count_stopwords,text_without_stopword, count_words


## MAIN ##

nltk_stopwords = set(stopwords.words('english'))
client = MongoClient('34.68.42.248:27017',authSource='reddit',username='admin',password='canito123')
db = client["reddit"]
commentsCollection = db["comments"]

try:
    consumer = KafkaConsumer(
   'Temas',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-1',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=["34.68.42.248:9091"])

    for comment in consumer:
        print(comment.value['postTitle'])

        upper,lower,vowel,consonant,stops, count_stopwords,text_without_stopword,count_words = upperLetters(comment.value['commentBody'])
        
        commentsCollection.insert_one(
        {    
            "id": comment.value['commentId'],
            "commentAuthor": comment.value['commentAuthor'], 
            "commentBody": comment.value['commentBody'], 
            "post":{
                "Id": comment.value['postId'],
                "Author": comment.value['postAuthor'], 
                "Title": comment.value['postAuthor'],
                "Score": comment.value['postScore'], 
                "Link": comment.value['postLink'], 
                "NumComments": comment.value['postNumComments']
            },
            
            "subredditTitle": comment.value['subredditTitle'],
            "stats":{
                "uppercase":upper,
                "lowercase":lower,
                "words":count_words,
                "vocals":vowel,
                "consonants":consonant,
                "stopwords":count_stopwords,
                "without_stops":text_without_stopword
            },     
        })
except expression as identifier:
    print('error')
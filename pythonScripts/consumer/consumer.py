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
    #nltk.download('stopwords')
    upper = 0
    lower = 0
    vowel = 0
    consonant = 0
    stops = 0
    vocals= ["a","e","i","o","u"]
    words = []

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
#nltk.download('stopwords')

nltk_stopwords = {'t', 'herself', 'm', 'more', 'is', 'those', 'doesn', "that'll", 'these', 'didn', 'by', 'from', 'haven', 'an', 'you', 'off', 'into', 'there', 'the', 'through', 'we', 'his', 'that', 'why', 'will', 'hers', 'o', "hadn't", "wasn't", "needn't", 'than', 'ourselves', 'in', 'again', 'it', 'does', 'weren', 'himself', 'same', 'isn', 'do', 'between', 'where', 'such', 'only', 'too', "couldn't", "hasn't", 've', "shouldn't", 'below', 'with', 'wouldn', 'been', "should've", 're', 'our', 'me', 'because', 'they', 'up', 'its', 'on', 'so', "don't", "won't", 'were', 'above', 'once', 'couldn', 'can', "aren't", "you'll", "weren't", 'while', 'y', 'd', 'itself', 'ain', 'are', 'what', 'any', 'as', 'yourself', 'mustn', "mustn't", 'my', 'other', 'yours', 'until', 'nor', 'further', 'about', 'them', 'to', 'both', 'her', 'who', 'some', 'doing', 'most', 'of', 'against', 'wasn', 'very', "doesn't", 'then', 'which', 'no', 'don', 'needn', 'him', 'each', 'now', "shan't", 'am', "you'd", "haven't", 'during', 'ma', 'for', 'hadn', 'or', 'theirs', 'did', 'but', 'just', 'all', 's', 'hasn', 'she', 'when', 'your', "you've", 'having', "mightn't", 'won', 'was', 'i', "she's", 'aren', 'he', 'if', 'own', 'at', 'a', 'down', 'not', 'myself', 'before', 'shouldn', 'had', 'themselves', 'whom', 'should', "didn't", 'be', 'has', 'll', "isn't", 'and', "you're", 'out', 'yourselves', 'have', 'under', 'ours', 'few', "wouldn't", 'here', 'how', "it's", 'over', 'their', 'shan', 'mightn', 'after', 'this', 'being'}

#print(nltk_stopwords)

client = MongoClient('35.202.48.205:27017',authSource='reddit',username='admin',password='canito123')
db = client["reddit"]
commentsCollection = db["comments"]

print("1")

try:
    consumer = KafkaConsumer(
   'Temas',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=["35.202.48.205:9091"])

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
                "Title": comment.value['postTitle'],
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
            "revisado":False     
        })
except expression as identifier:
    print('error')
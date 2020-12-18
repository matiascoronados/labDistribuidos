from kafka import KafkaConsumer
from json import loads

import pymongo
from pymongo import MongoClient
from pymongo import *

client = MongoClient('34.68.42.248:27017',authSource='reddit',username='admin',password='canito123')#datos de conexion de bd
db = client["reddit"]#asi se accede a una bd
commentsCollection = db["comments"]#asi se accede a una coleccion


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
                "uppercase":0,
                "lowercase":0,
                "words":0,
                "vocals":0,
                "consonants":0,
                "stopwords":0,
                "without_stops":""
            },
        
            
        })
except expression as identifier:
    print('error')

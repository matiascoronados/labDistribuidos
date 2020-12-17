from kafka import KafkaConsumer
from json import loads

import pymongo
from pymongo import MongoClient
from pymongo import *

client = MongoClient('localhost:27017',authSource='reddit')#datos de conexion de bd
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
            "commentId": comment.value['commentId'],
            "commentAuthor": comment.value['commentAuthor'], 
            "commentBody": comment.value['commentBody'], 
            "postId": comment.value['postId'],
            "postAuthor": comment.value['postAuthor'], 
            "postTitle": comment.value['postAuthor'],
            "postScore": comment.value['postScore'], 
            "postLink": comment.value['postLink'], 
            "postNumComments": comment.value['postNumComments'], 
            "subredditTitle": comment.value['subredditTitle']
        })
except expression as identifier:
    print('error')

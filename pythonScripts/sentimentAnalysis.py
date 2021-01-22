from textblob import TextBlob
import pymongo
from pymongo import MongoClient
from pymongo import *
from pretty import pprint
import nltk
import psycopg2
def analysisScore(text):
    #print(text['without_stops'])
    print("comentario")
    blob = TextBlob(text['without_stops'])
    tag = blob.tags
    noun_phrases = blob.noun_phrases
    dataCount = 0
    sumCount = 0
    for sentence in blob.sentences:
        dataCount = dataCount +1
        sumCount = sentence.sentiment.polarity + sumCount
        
        #mean = mean(sentence.sentiment.polarity)
    promedio = sumCount / dataCount
    #print(promedio) 
    return promedio  
        
    
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
client = MongoClient('34.68.42.248', username='admin', password='canito123', authSource='reddit', authMechanism='SCRAM-SHA-1')#datos de conexion de bd
#client = MongoClient('mongodb://riruriru:riruriru@35.239.147.51:27017/?authSource=admin&readPreference=primary&ssl=false')
db = client["reddit"]#asi se accede a una bd
collection = db["comments"]#asi se accede a una coleccion

conn = psycopg2.connect(database='reddit', user='postgres',password='canito123', host='34.121.166.27', port= '55432');


#Setting auto commit false
conn.autocommit = True
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#cursor.execute("INSERT INTO topics(id_topic,topic_title) VALUES ('1','hola')")


cursor.execute("SELECT %s FROM topics WHERE id_topic=%s",(1,2))
a = cursor.fetchone()
print(a)


dataDB = collection.find()

cursor.close()
conn.close()


"""for comment in dataDB:
    #print(comment)
    sentimentValue = analysisScore(comment['stats'])

    #a = cursor.execute("SELECT EXISTS(SELECT 1 FROM topics WHERE topic_title="+comment['subredditTitle']+")")
    a = cursor.execute("SELECT 1 FROM topics WHERE id_topic=1")

    print(a)"""
    




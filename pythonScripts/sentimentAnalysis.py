from textblob import TextBlob
import pymongo
from pymongo import MongoClient
from pymongo import *
from pretty import pprint
import nltk
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
    print(promedio)   
        
    

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
client = MongoClient('34.68.42.248', username='admin', password='canito123', authSource='reddit', authMechanism='SCRAM-SHA-1')#datos de conexion de bd
#client = MongoClient('mongodb://riruriru:riruriru@35.239.147.51:27017/?authSource=admin&readPreference=primary&ssl=false')
db = client["reddit"]#asi se accede a una bd
collection = db["comments"]#asi se accede a una coleccion

dataDB = collection.find()
for comment in dataDB:
    #print(comment)
    analysisScore(comment['stats'])
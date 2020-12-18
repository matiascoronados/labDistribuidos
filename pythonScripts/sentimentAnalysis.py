from langdetect import detect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import nltk
import pymongo
from pymongo import MongoClient
from pymongo import *
from pretty import pprint

nltk_stopwords = set(stopwords.words('english'))

def stopwords(text):
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

def upperLetters(dataDB,collection):
#    nltk.download('stopwords')
    upper = 0
    lower = 0
    vowel = 0
    consonant = 0
    stops = 0
    vocals= ["a","e","i","o","u"]

    words =[]
    for comment in dataDB:
        newComment = comment
        #print(comment["commentBody"])
        for letter in comment["commentBody"]:
            if(letter.isupper()):
                upper+=1
            elif(letter.islower()):
                lower+=1
            if(letter in vocals):
                vowel+=1
            else:
                consonant+=1
        count_stopwords, text_without_stopword = stopwords(comment["commentBody"])

        words = comment["commentBody"].split(" ")
        count_words = len(words)   
        #update comment stats        
        collection.update_one({"_id":comment["_id"]} ,{"$set":{
            "stats.uppercase": upper,
            "stats.lowercase": lower,
            "stats.vocals": vowel,
            "stats.words": count_words,
            "stats.consonants":consonant,
            "stats.stopwords": count_stopwords,
            "stats.without_stops":text_without_stopword
        } })




client = MongoClient('34.68.42.248', username='admin', password='canito123', authSource='reddit', authMechanism='SCRAM-SHA-1')#datos de conexion de bd
#client = MongoClient('mongodb://riruriru:riruriru@35.239.147.51:27017/?authSource=admin&readPreference=primary&ssl=false')
db = client["reddit"]#asi se accede a una bd
collection = db["comments"]#asi se accede a una coleccion

dataDB = collection.find()

upperLetters(dataDB,collection)


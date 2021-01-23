from textblob import TextBlob
import pymongo
from pymongo import MongoClient
from pymongo import *
from pretty import pprint
import nltk
import psycopg2
def analysisScore(text):
    #print(text['without_stops'])
    #print("comentario")
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
        
    
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')
client = MongoClient('34.70.222.160', username='admin', password='canito123', authSource='reddit', authMechanism='SCRAM-SHA-1')#datos de conexion de bd
#client = MongoClient('mongodb://riruriru:riruriru@35.239.147.51:27017/?authSource=admin&readPreference=primary&ssl=false')
db = client["reddit"]#asi se accede a una bd
collection = db["comments"]#asi se accede a una coleccion

conn = psycopg2.connect(database='reddit', user='postgres',password='canito123', host='34.121.166.27', port= '55432');


#Setting auto commit false
conn.autocommit = True
#Creating a cursor object using the cursor() method
cursor = conn.cursor()


dataDB = collection.find()



for comment in dataDB:


    # Variables 

    sentimentValue = analysisScore(comment['stats'])
    aux=comment['post']['Title'].replace("'","")
    cursor.execute("SELECT EXISTS(SELECT 1 FROM topics WHERE topic_title='"+aux+"')")
    queryTopicExist = cursor.fetchone()[0]


    if(queryTopicExist):
        print("Si esta")

        #cursor.execute("SELECT id_topic FROM topics WHERE topic_title='"+comment['subredditTitle']+"'")
        #idTopic = cursor.fetchone()[0]
        #print(idTopic)
        

    else:
        print("No esta")

        # Insertar Topico
        cursor.execute("INSERT INTO topics(id_topic,topic_title) VALUES (DEFAULT,'"+comment['subredditTitle'].replace("'","")+"') RETURNING id_topic")
        id_topic = cursor.fetchone()[0]
        #print(id_topic)

        aux=comment['post']['Title'].replace("'","")
        aux=aux[0:500]
        print(aux)
        # Insertar Post
        cursor.execute("""INSERT INTO posts (id_post, id_topic, post_title, post_author, post_score, post_link, post_numcomments) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                (comment['post']['Id'], id_topic, aux, comment['post']['Author'], comment['post']['Score'], comment['post']['Link'], comment['post']['NumComments']))

        # Insertar Comentario
        cursor.execute("""INSERT INTO comments(id_comment, id_post, comment_author, comment_body, sentiment_value) 
                VALUES (%s, %s, %s, %s, %s)""", 
                (comment['post']['Id'], comment['post']['Id'], comment['commentAuthor'], comment['commentBody'][0:500], sentimentValue))

cursor.close()
conn.close()



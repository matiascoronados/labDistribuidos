from textblob import TextBlob
import pymongo
from pymongo import MongoClient
from pymongo import *
import nltk
import psycopg2
import time


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
    
    if(dataCount!=0):
        promedio = sumCount / dataCount
    else:
        promedio = 0
    #print(promedio) 
    return promedio  
        


#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')
client = MongoClient('35.202.48.205', username='admin', password='canito123', authSource='reddit', authMechanism='SCRAM-SHA-1')#datos de conexion de bd
#client = MongoClient('mongodb://riruriru:riruriru@35.239.147.51:27017/?authSource=admin&readPreference=primary&ssl=false')
db = client["reddit"]#asi se accede a una bd
collection = db["comments"]#asi se accede a una coleccion

conn = psycopg2.connect(database='reddit', user='postgres',password='canito123', host='34.121.166.27', port= '55432');

#Setting auto commit false
conn.autocommit = True
#Creating a cursor object using the cursor() method
cursor = conn.cursor()


dataDB = collection.find()


<<<<<<< HEAD
#cursor.execute("DELETE FROM comments")
#cursor.execute("DELETE FROM posts")
#cursor.execute("DELETE FROM topics")

while True:
    for comment in dataDB:
        if(comment['revisado'] == False):
            # Variables 
            sentimentValue = analysisScore(comment['stats'])
            topic_title = comment['subredditTitle'].replace("'","")[0:499]
            post_title = comment['post']['Title'].replace("'","")[0:499]
            post_author = comment['post']['Author'].replace("'","")[0:29]
            comment_author = comment['commentAuthor'].replace("'","")[0:29]
            comment_body = comment['commentBody'].replace("'","")[0:599]

            cursor.execute("SELECT EXISTS(SELECT 1 FROM topics WHERE topic_title='"+topic_title+"')")
            queryTopicExist = cursor.fetchone()[0]


            if(queryTopicExist):
                print("Si esta")
                cursor.execute("SELECT EXISTS(SELECT 1 FROM posts WHERE id_post='"+comment['post']['Id']+"')")
                queryPostExist = cursor.fetchone()[0]

                #Se verifica si existe el post
                if(not queryPostExist):
                    #Se obtiene el ID del topico
                    cursor.execute("SELECT id_topic FROM topics WHERE topic_title = '"+topic_title+"'")
                    id_topic = cursor.fetchone()[0]
                    #Se crea el post
                    cursor.execute("""INSERT INTO posts (id_post, id_topic, post_title, post_author, post_score, post_link, post_numcomments) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                            (comment['post']['Id'], id_topic, post_title, post_author, comment['post']['Score'], comment['post']['Link'], comment['post']['NumComments']))

                #Se agrega el comentario
                cursor.execute("""INSERT INTO comments(id_comment, id_post, comment_author, comment_body, sentiment_value) 
                        VALUES (%s, %s, %s, %s, %s)""", 
                        (comment['id'], comment['post']['Id'], comment_author, comment_body, sentimentValue))

            else:
                print("No esta")

                # Insertar Topico
                cursor.execute("INSERT INTO topics(id_topic,topic_title) VALUES (DEFAULT,'"+topic_title+"') RETURNING id_topic")
                id_topic = cursor.fetchone()[0]
        
                # Insertar Post
                cursor.execute("""INSERT INTO posts (id_post, id_topic, post_title, post_author, post_score, post_link, post_numcomments) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                        (comment['post']['Id'], id_topic, post_title, post_author, comment['post']['Score'], comment['post']['Link'], comment['post']['NumComments']))

                # Insertar Comentario
                cursor.execute("""INSERT INTO comments(id_comment, id_post, comment_author, comment_body, sentiment_value) 
                        VALUES (%s, %s, %s, %s, %s)""", 
                        (comment['id'], comment['post']['Id'], comment_author, comment_body, sentimentValue))

            collection.update({
            'id': comment['id']},
            {'$set':{
                'revisado':True
            }},upsert=False,multi=False)
    time.sleep(2)
=======
cursor.execute("DELETE FROM comments")
cursor.execute("DELETE FROM posts")
cursor.execute("DELETE FROM topics")


for comment in dataDB:

    # Variables 
    sentimentValue = analysisScore(comment['stats'])
    topic_title = comment['subredditTitle'].replace("'","")[0:499]
    post_title = comment['post']['Title'].replace("'","")[0:499]
    post_author = comment['post']['Author'].replace("'","")[0:29]
    comment_author = comment['commentAuthor'].replace("'","")[0:29]
    comment_body = comment['commentBody'].replace("'","")[0:599]

    cursor.execute("SELECT EXISTS(SELECT 1 FROM topics WHERE topic_title='"+topic_title+"')")
    queryTopicExist = cursor.fetchone()[0]

    if(queryTopicExist):
        print("Si esta")
        cursor.execute("SELECT EXISTS(SELECT 1 FROM posts WHERE id_post='"+comment['post']['Id']+"')")
        queryPostExist = cursor.fetchone()[0]

        #Se verifica si existe el post
        if(not queryPostExist):
            #Se obtiene el ID del topico
            cursor.execute("SELECT id_topic FROM topics WHERE topic_title = '"+topic_title+"'")
            id_topic = cursor.fetchone()[0]
            #Se crea el post
            cursor.execute("""INSERT INTO posts (id_post, id_topic, post_title, post_author, post_score, post_link, post_numcomments) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                    (comment['post']['Id'], id_topic, post_title, post_author, comment['post']['Score'], comment['post']['Link'], comment['post']['NumComments']))

        #Se agrega el comentario
        cursor.execute("SELECT EXISTS(SELECT 1 FROM comments WHERE id_comment='"+comment['id']+"')")
        queryCommentExist = cursor.fetchone()[0]
        if(not queryCommentExist):    
            cursor.execute("""INSERT INTO comments(id_comment, id_post, comment_author, comment_body, sentiment_value) 
                    VALUES (%s, %s, %s, %s, %s)""", 
                    (comment['id'], comment['post']['Id'], comment_author, comment_body, sentimentValue))

    else:
        print("No esta")

        # Insertar Topico
        cursor.execute("INSERT INTO topics(id_topic,topic_title) VALUES (DEFAULT,'"+topic_title+"') RETURNING id_topic")
        id_topic = cursor.fetchone()[0]
 
        # Insertar Post
        cursor.execute("""INSERT INTO posts (id_post, id_topic, post_title, post_author, post_score, post_link, post_numcomments) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                (comment['post']['Id'], id_topic, post_title, post_author, comment['post']['Score'], comment['post']['Link'], comment['post']['NumComments']))

        # Insertar Comentario
        cursor.execute("""INSERT INTO comments(id_comment, id_post, comment_author, comment_body, sentiment_value) 
                VALUES (%s, %s, %s, %s, %s)""", 
                (comment['id'], comment['post']['Id'], comment_author, comment_body, sentimentValue))

>>>>>>> main
cursor.close()
conn.close()



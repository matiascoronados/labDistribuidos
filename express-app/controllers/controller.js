const { Pool } = require('pg')
const { response } = require('express');

const pool = new Pool({
    host: '34.121.166.27',
    user: 'postgres',
    password:'canito123',
    database: 'reddit',
    port:'55432' 
})

const getAllComments = (request,response) => {
    pool.query('SELECT * FROM comments',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}
const getAllPosts = (request,response) => {
    pool.query('SELECT * FROM posts',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}
const getAllTopics = (request,response) => {
    pool.query('SELECT * FROM topics',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}

const getPostsWithMoreComments = (request,response) => {
    pool.query('SELECT posts.id_post,posts.post_title,posts.post_numcomments FROM posts ORDER BY posts.post_numcomments DESC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}

const getTopicsWithMoreComments = (request,response) => {
    pool.query('SELECT topics.id_topic,topics.topic_title, SUM(posts.post_numcomments) AS cantidad_comentarios FROM topics LEFT JOIN posts ON topics.id_topic = posts.id_topic GROUP BY topics.id_topic ORDER BY cantidad_comentarios DESC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}

const getTopicsWithMorePost = (request,response) => {
    pool.query('SELECT topics.id_topic,topics.topic_title, COUNT(*) AS cantidad_posts FROM topics LEFT JOIN posts ON topics.id_topic = posts.id_topic GROUP BY topics.id_topic ORDER BY cantidad_posts DESC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}

const getScoreFromTopic = (request,response) => {
    pool.query('SELECT topics.id_topic,topics.topic_title, SUM(posts.post_score) AS scorePost FROM topics LEFT JOIN posts ON topics.id_topic = posts.id_topic GROUP BY topics.id_topic ORDER BY scorePost DESC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}

const getScoreFromPost = (request,response) => {
    pool.query('SELECT * FROM posts ORDER BY posts.post_score DESC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}

const getPositivePost = (request,response) => {
    pool.query('SELECT posts.id_post, posts.post_title, COUNT(*) AS cantidad_comentarios ,AVG(comments.sentiment_value) AS sentiment FROM posts LEFT JOIN comments ON posts.id_post = comments.id_post GROUP BY posts.id_post ORDER BY sentiment DESC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}


const getNegativePost = (request,response) => {
    pool.query('SELECT posts.id_post, posts.post_title, COUNT(*) AS cantidad_comentarios ,AVG(comments.sentiment_value) AS sentiment FROM posts LEFT JOIN comments ON posts.id_post = comments.id_post GROUP BY posts.id_post ORDER BY sentiment ASC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}

const getPositiveTopic = (request,response) => {
    pool.query('SELECT topics.id_topic, topics.topic_title, AVG(comments.sentiment_value) AS sentiment FROM topics,posts,comments WHERE topics.id_topic = posts.id_topic AND posts.id_post = comments.id_post GROUP BY topics.id_topic ORDER BY sentiment DESC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}

const getNegativeTopic = (request,response) => {
    pool.query('SELECT topics.id_topic, topics.topic_title, AVG(comments.sentiment_value) AS sentiment FROM topics,posts,comments WHERE topics.id_topic = posts.id_topic AND posts.id_post = comments.id_post GROUP BY topics.id_topic ORDER BY sentiment ASC LIMIT 10',(error,results) =>{
        if(error){
            throw error
        }
        response.status(200).send(results);
    })
}


//Exportar Funciones

module.exports={
    getAllComments,
    getAllPosts,
    getAllTopics,
    getPostsWithMoreComments,
    getTopicsWithMoreComments,
    getTopicsWithMorePost,
    getScoreFromTopic,
    getScoreFromPost,
    getPositivePost,
    getNegativePost,
    getPositiveTopic,
    getNegativeTopic
}
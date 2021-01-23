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



//Exportar Funciones

module.exports={
    getAllComments,
    getAllPosts,
    getAllTopics
}
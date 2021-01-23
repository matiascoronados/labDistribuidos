DROP DATABASE IF EXISTS reddit;
CREATE DATABASE reddit;


DROP TABLE IF EXISTS topics;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;

CREATE TABLE topics(
    id_topic SERIAL PRIMARY KEY,
    topic_title VARCHAR(500) NOT NULL
);

CREATE TABLE posts(
    id_post VARCHAR(20) NOT NULL PRIMARY KEY,
    id_topic INT,
    post_title VARCHAR(500) NOT NULL,
    post_author VARCHAR(30) NOT NULL,
    post_score INT NOT NULL,
    post_link VARCHAR(200) NOT NULL,
    post_numComments INT NOT NULL,
    CONSTRAINT fk_topic
        FOREIGN KEY(id_topic) 
            REFERENCES topics(id_topic)
);

CREATE TABLE comments(
    id_comment VARCHAR(20) NOT NULL PRIMARY KEY,
    id_post VARCHAR(20),
    comment_author VARCHAR(30) NOT NULL,
    comment_body VARCHAR(600) NOT NULL,
    sentiment_value DECIMAL,
    CONSTRAINT fk_post
        FOREIGN KEY(id_post) 
            REFERENCES posts(id_post)
);














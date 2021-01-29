const { Router } = require('express');
const router = Router();


const {
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
    getNegativeTopic,
    getAllPositiveAndNegativeComments,
    getAllPositiveAndNegativePosts,
    getAllPositiveAndNegativeTopics
} = require('../controllers/controller')

router.get('/getAllComments',getAllComments)
router.get('/getAllPosts',getAllPosts)
router.get('/getAllTopics',getAllTopics)
router.get('/getPostsWithMoreComments',getPostsWithMoreComments)
router.get('/getTopicsWithMoreComments',getTopicsWithMoreComments)
router.get('/getTopicsWithMorePost',getTopicsWithMorePost)
router.get('/getScoreFromTopic',getScoreFromTopic)
router.get('/getScoreFromPost',getScoreFromPost)
router.get('/getPositivePost',getPositivePost)
router.get('/getNegativePost',getNegativePost)
router.get('/getPositiveTopic',getPositiveTopic)
router.get('/getNegativeTopic',getNegativeTopic)
router.get('/getAllPositiveAndNegativeComments',getAllPositiveAndNegativeComments)
router.get('/getAllPositiveAndNegativePosts',getAllPositiveAndNegativePosts)
router.get('/getAllPositiveAndNegativeTopics',getAllPositiveAndNegativeTopics)

module.exports = router;
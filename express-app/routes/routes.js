const { Router } = require('express');
const router = Router();


const {getAllComments,getAllPosts,getAllTopics} = require('../controllers/controller')

router.get('/comments',getAllComments)
router.get('/posts',getAllPosts)
router.get('/topics',getAllTopics)


module.exports = router;
<template>
<div class="container">
    <div class="columns is-mobile">
        <div class="column is-three-fifths is-offset-one-fifth">
            
            <div class="card">
                <h4>Post más Comentados</h4>
                <bar-top-post-comments/>
            </div>
        </div>
        
        
    </div>
    <div class="column is-three-fifths is-offset-one-fifth">
            
            <div class="card">
                <h4>Top Score de Posts</h4>
                <post-score/>
            </div>
        </div>
    <div class="column is-three-fifths is-offset-one-fifth">
            
            <div class="card">
                <h4>Positividad de Post</h4>
                <positive-posts/>
            </div>
        </div>
    <div class="column is-three-fifths is-offset-one-fifth">
            
            <div class="card">
                <h4>Negatividad de Post</h4>
                <negative-posts/>
            </div>
        </div>
</div>
</template>

<script>
import BarTopPostComments from '../components/Posts/barTopPostComments.vue'
import NegativePosts from '../components/Posts/NegativePosts.vue'
import PositivePosts from '../components/Posts/PositivePosts.vue'
import PostScore from '../components/Posts/PostScore.vue'
export default {
    components:{
        
        BarTopPostComments,
        PostScore,
        PositivePosts,
        NegativePosts
    }
}
</script>,
        PositivePosts
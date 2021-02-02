<template>
<div class="container">
    <div class="columns">
        <div class="column is-three-fifths is-offset-one-fifth">
            
            <div class="card">
                <h4>Tópicos más Comentados</h4>
                <bar-top-topics-comments/>
            </div>
        </div>
        
    </div>
    <div class="columns">
        <div class="column">
            <div class="card">
            <h4 class="mt-3">Cantidad de Post por Tópico</h4>    
            <get-post-of-topics/>
            </div>
        </div>    
        <div class="column">
            <div class="card">
            <h4 class="mt-3">Score de topicos</h4>    
            <topic-score/>
            </div>
        </div>
    </div>
    <div class="columns">
        <div class="column">
            <div class="card">
            <h4 class="mt-3">Topicos Positivos</h4>    
            <positive-topics/>
            </div>
        </div>
        <div class="column">
            <div class="card">
            <h4 class="mt-3">Negatividad de topicos</h4>    
            <negative-topics/>
            </div>
        </div>
    </div>  
</div>
</template>

<script>
import BarTopTopicsComments from '../components/Topics/barTopTopicsComments.vue'
import GetPostOfTopics from '../components/Topics/getPostOfTopics.vue'
import NegativeTopics from '../components/Topics/NegativeTopics.vue'
import PositiveTopics from '../components/Topics/PositiveTopics.vue'
import TopicScore from '../components/Topics/TopicScore.vue'
export default {
    components:{
        
        BarTopTopicsComments,
        GetPostOfTopics,
        TopicScore,
        NegativeTopics,
        PositiveTopics,

    }
}
</script>
<template>
<div class="container">
  <div class="columns">
    <div class="column">
      <h2>Topicos</h2>
      <pie-topics/>
    </div>
    <div class="column">
        <h2>Posts</h2>
        <pie-posts/>
      </div>
    <div class="column">
      <h2> Comentarios</h2>
      <pie-comments/>
    </div>
  </div>  
  
  <div class="columns">
    
  </div>
      <Table/>
  
</div>
</template>

<script>
import PieComments from '../components/PieComments.vue'
import PiePosts from '../components/PiePosts.vue'
import PieTopics from '../components/PieTopics.vue'
import Table from '../components/Table.vue'


export default {
  components: { PiePosts, PieTopics, PieComments,Table },

}
</script>
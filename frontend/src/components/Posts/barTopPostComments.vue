<template>
  <div>
  <apexchart ref="topcomments" width="500" type="bar" :options="options" :series="series"></apexchart>
  </div>
</template>
<script>
import axios from 'axios'
export default{
  
data(){
    return {
      data: [],
      options: {
        plotOptions:{
          bar:{
            horizontal:true
          }
        },
        chart: {
          id: 'vuechart-example',
         
        },
        xaxis: {
          categories: []
        }
      },
      noData:{
        text:'loading...'
      },
      series: [{
        name: 'comentarios',
        data: []
      }],
    }
  },
  methods:{
    getChartData(){
      const url = 'http://34.72.32.60:3000/getPostsWithMoreComments'
      axios.get(url).then(response=>{
        
        this.data = response.data["rows"]
        //nombre de los post en el eje x
        for(var i = 0; i<10;i++){
          this.options.xaxis.categories.push(this.data[i]["post_title"])
        }

        //actualizar con axios
        let series = []
        console.log(this.data)
        this.data.forEach(element=>{
          series.push(element["post_numcomments"])
        })
        
        this.$refs.topcomments.updateSeries([{
          name:'comentarios',
          data: series
        }])
        console.log(this.series)
      })
    }
  },
  mounted(){
    this.getChartData()
  },
  
}
</script>
<template>
  <div>
  <apexchart ref="topcomments" width="600" type="bar" :options="options" :series="series"></apexchart>
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
      const url = 'http://35.224.174.197:3000/getTopicsWithMoreComments'
      axios.get(url).then(response=>{
        
        this.data = response.data["rows"]
        //nombre de los post en el eje x
        for(var i = 0; i<10;i++){
          this.options.xaxis.categories.push(this.data[i]["topic_title"])
        }

        //actualizar con axios
        let series = []
        console.log(this.data)
        this.data.forEach(element=>{
          series.push(element["cantidad_comentarios"])
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
<template>
    <apexchart ref="topicpost" width="500" type="bar" :options="options" :series="series"></apexchart>
</template>
<script>
import axios from 'axios'
export default {
    data(){
        return{
        data: [],
      options: {
        plotOptions:{
          bar:{
            horizontal:false
          }
        },
        chart: {
          id: 'vuechart-example',
         
        },
        fill:{
            colors:['#F39C12']
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
            const url = 'http://35.224.174.197:3000/getScoreFromPost'
            axios.get(url).then(response=>{
                this.data = response.data["rows"]
                //prepare x axis
                for(var i =0 ; i<10; i++){
                    this.options.xaxis.categories.push(this.data[i]["post_title"])
                }
                let series = []
                this.data.forEach(element=>{
                    series.push(element["post_score"])
                })
                console.log(series)
                this.$refs.topicpost.updateSeries([{
                name:'Score',
                data: series
                }])
            })
        }
    },
    mounted(){
        this.getChartData()
    }
}
</script>
<template>
    <apexchart ref="topicscore" width="600" type="bar" :options="options" :series="series"></apexchart>
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
            const url = 'http://34.72.210.185:3000/getScoreFromTopic'
            axios.get(url).then(response=>{
                this.data = response.data["rows"]
                //prepare x axis
                for(var i =0 ; i<10; i++){
                    this.options.xaxis.categories.push(this.data[i]["topic_title"])
                }
                let series = []
                this.data.forEach(element=>{
                    series.push(element["scorepost"])
                })
                console.log(series)
                this.$refs.topicscore.updateSeries([{
                name:'Cantidad Post',
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
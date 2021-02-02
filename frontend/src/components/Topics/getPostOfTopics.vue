<template>
    <apexchart ref="postoftopics" width="600" type="bar" :options="options" :series="series"></apexchart>
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
            colors:['#76448A']
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
            const url = 'http://35.224.174.197:3000/getTopicsWithMorePost'
            axios.get(url).then(response=>{
                this.data = response.data["rows"]
                //prepare x axis
                for(var i =0 ; i<10; i++){
                    this.options.xaxis.categories.push(this.data[i]["topic_title"])
                }
                let series = []
                this.data.forEach(element=>{
                    series.push(element["cantidad_posts"])
                })
                console.log(series)
                this.$refs.postoftopics.updateSeries([{
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
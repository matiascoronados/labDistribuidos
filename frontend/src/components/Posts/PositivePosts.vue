<template>
    <apexchart ref="positivetopics" width="600" type="bar" :options="options" :series="series"></apexchart>
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
            horizontal:true
          }
        },
        chart: {
          id: 'vuechart-example',
         
        },
        fill:{
            colors:['#17A589']
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
            const url = 'http://34.72.210.185:3000/getPositivePost'
            axios.get(url).then(response=>{
                this.data = response.data["rows"]
                //prepare x axis
                for(var i =0 ; i<10; i++){
                    this.options.xaxis.categories.push(this.data[i]["post_title"])
                }
                let series = []
                this.data.forEach(element=>{
                    series.push(element["sentiment"])
                })
                console.log(series)
                this.$refs.positivetopics.updateSeries([{
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
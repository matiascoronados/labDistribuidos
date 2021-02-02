<template>
    <apexchart ref="negativeposts" width="500" type="bar" :options="options" :series="series"></apexchart>
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
            colors:['#E74C3C']
        },
        xaxis: {
          categories: []
        }
      },
      noData:{
        text:'loading...'
      },
      series: [{
        name: 'Negatividad',
        data: []
      }],
        }
    },
    methods:{
        getChartData(){
            const url = 'http://35.224.174.197:3000/getNegativePost'
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
                this.$refs.negativeposts.updateSeries([{
                name:'Negatividad',
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
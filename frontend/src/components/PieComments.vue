<template>
    <div>
     <apexchart width="400" ref="piecomments" type="pie" :options="chartOptions" :series="series"></apexchart>
   </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
      return {
          series: [],
        data : [],
        chartOptions: {
            chart: {
              width: 400,
              type: 'pie',
            },
          labels: [],
          colors: ["#1ABC9C","#FF4500"]
        },
        
       
      }
    },
    methods:{
      getChartData(){
        const url = 'http://35.224.174.197:3000/getAllPositiveAndNegativeComments';
        axios.get(url).then(response=>{
            this.data = response.data["rows"]
            //console.log(this.data)
            
            this.chartOptions.labels.push("Comentarios Positivos")
            this.chartOptions.labels.push("Comentarios Negativos")
            //this.series.push( this.data[0]["comments_positivos"])
            //this.series.push( this.data[0]["comments_negativos"])
            var series = [parseInt(this.data[0]["comments_positivos"]),parseInt( this.data[0]["comments_negativos"])]
            console.log(series)
            this.$refs.piecomments.updateSeries(series)
            

        })
      }
    },
    mounted(){
        this.getChartData()
    }
};
</script>
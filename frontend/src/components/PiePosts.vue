<template>
    <div>
     <apexchart width="380" ref="piepost" type="pie" :options="chartOptions" :series="series"></apexchart>
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
              width: 380,
              type: 'pie',
            },
          labels: [],
          colors: ["#1ABC9C","#FF4500"]
        },
        
       
      }
    },
    methods:{
      getChartData(){
        const url = 'http://34.72.32.60:3000/getAllPositiveAndNegativePosts';
        axios.get(url).then(response=>{
            this.data = response.data["rows"]
            //console.log(this.data)
            
            this.chartOptions.labels.push("Posts Positivos")
            this.chartOptions.labels.push("Posts Negativos")
            //this.series.push( this.data[0]["comments_positivos"])
            //this.series.push( this.data[0]["comments_negativos"])
            var series = [parseInt(this.data[0]["positivepost"]),parseInt( this.data[0]["negativepost"])]
            console.log(series)
            this.$refs.piepost.updateSeries(series)
            

        })
      }
    },
    mounted(){
        this.getChartData()
    }
};
</script>
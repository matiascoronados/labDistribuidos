import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueApexCharts from 'vue-apexcharts'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

Vue.config.productionTip = false
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)
Vue.use(Buefy)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

import Vue from 'vue'
import App from './App.vue'
// import router from './router'
// import store from './store'

Vue.config.productionTip = false

import Alert from "./plugin/alert/index"
import Loading from "./plugin/load/index"
Vue.use( Alert, {
  container: "#app"
})
Vue.use( Loading, {
  container: "#app"
})


new Vue({
  // router,
  // store,
  render: h => h(App)
}).$mount('#app')

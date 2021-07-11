import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'


Vue.config.productionTip = false

new Vue({
  router,
  store,
  // @ts-ignore
  render: h => h(App)
  
}).$mount('#app')

// new Vue({

//   components: { App },
//   router,
//   store
// }).$mount('#app')
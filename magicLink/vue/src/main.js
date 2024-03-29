import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Amplify from '@aws-amplify/core'
import awsconfig from './aws-exports';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import "./assets/styles/cognito-login.css";


Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Amplify.configure(awsconfig);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

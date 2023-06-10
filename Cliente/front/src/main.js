import Vue from 'vue'
import { createPinia, PiniaVuePlugin } from 'pinia'
import App from './App.vue'
import router from './router'
import "bootstrap";
import VueSweetalert2 from 'vue-sweetalert2';
import axios from 'axios'
import VueAxios from 'vue-axios'
import '@/assets/scripts/login.js'

import '@/assets/Material/css/styles.css'
import '@/assets/Material/js/material.js'
import '@/assets/Material/js/bootstrap.bundle.min.js'
import '@/assets/Material/js/scripts.js'

//Fuentes de letra de google 
import '@/assets/Material/assets/fonts/font1.css'
import '@/assets/Material/assets/fonts/font2.css'
import '@/assets/Material/assets/fonts/font3.css'

import "bootstrap/dist/css/bootstrap.min.css";
import 'sweetalert2/dist/sweetalert2.min.css';

Vue.use(VueAxios, axios)
Vue.use(VueSweetalert2);
Vue.use(PiniaVuePlugin)
const pinia = createPinia()

Vue.config.productionTip = false
new Vue({
  router,
  pinia,
  render: h => h(App)
}).$mount('#app')

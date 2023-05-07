import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Semaforos from '../views/Semaforos.vue'
import LogIn from '../views/LogIn.vue'
import Configuracion from '../views/ConfiguracionModo.vue'
import RegistarSemaforo from '@/views/RegistarSemaforo.vue'
import RegistarUsuario from '@/views/RegistarUsuario.vue'
import ListaSemaforos from '@/views/ListaSemaforos.vue'
import ListaUsuarios from '@/views/ListaUsuarios.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/listasemaforos',
    name:'ListaSemaforos',
    component:ListaSemaforos
  },
  {
    path:'/listausuarios',
    name:'ListaUsuarios',
    component:ListaUsuarios
  },
  {
    path:'/Semaforo',
    name:'Semaforos',
    component:Semaforos
  },
  {
    path:'/login',
    name:'login',
    component:LogIn
  },
  {
    path:'/configuracion',
    name:'ConfiguracionModo',
    component:Configuracion
  },
  {
    path:'/registarsemaforo',
    name:'RegistarSemaforo',
    component:RegistarSemaforo
  },
  {
    path:'/registarusuario',
    name:'RegistarUsuario',
    component:RegistarUsuario
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

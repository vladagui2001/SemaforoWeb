<template>
    <div id="app">
      <body class="nav-fixed bg-light">
      <nav class="top-app-bar navbar navbar-expand navbar-dark bg-dark">
            <div class="container-fluid px-4">
                <button class="btn btn-lg btn-icon order-1 order-lg-0" id="drawerToggle" href="javascript:void(0);"><i class="material-icons">menu</i></button>
                <!-- Navbar de control Semáforos-->
                <a class="navbar-brand me-auto" href="/"><div class="text-uppercase font-monospace">Control de Semáforos</div></a>
                <div class="d-flex align-items-center mx-3 me-lg-0">
                    <ul class="navbar-nav d-none d-lg-flex">
                        <li class="nav-item"><a class="nav-link" href="#">Opciones</a></li>
                        <li class="nav-item"><a class="nav-link" href="/login">Iniciar Sesión/Cerrar Sesión</a></li>
                    </ul>        
                </div>
            </div>
        </nav>
        <div id="layoutDrawer">
            <div id="layoutDrawer_nav">
                <nav class="drawer accordion drawer-light bg-white" id="drawerAccordion">
                    <div class="drawer-menu">
                        <div class="nav">
                            <div class="drawer-menu-divider d-sm-none"></div>

                            <!-- Administración de Usuarios-->
                            <div class="drawer-menu-heading">Administración de Usuarios</div>

                            <!-- Opciones Semáforos-->
                            <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseSemaforos" aria-expanded="false" aria-controls="collapseDashboards">
                                <div class="nav-link-icon"><i class="material-icons">dashboard</i></div>
                                Semáforos
                                <div class="drawer-collapse-arrow"><i class="material-icons">expand_more</i></div>
                            </a>
                            <!-- Subopciones Semáforos -->
                            <div class="collapse" id="collapseSemaforos" aria-labelledby="headingOne" data-bs-parent="#drawerAccordion">
                                <nav class="drawer-menu-nested nav">
                                    <a class="nav-link" href="/Semaforo">Ver Semáforos</a>
                                </nav>
                            </div>

                            <!-- Opciones Usuarios-->
                            <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseUsuarios" aria-expanded="false" aria-controls="collapseDashboards">
                                <div class="nav-link-icon"><i class="material-icons">person</i></div>
                                Usuarios
                                <div class="drawer-collapse-arrow"><i class="material-icons">expand_more</i></div>
                            </a>
                            <!-- Subopciones Usuarios -->
                            <div class="collapse" id="collapseUsuarios" aria-labelledby="headingOne" data-bs-parent="#drawerAccordion">
                                <nav class="drawer-menu-nested nav">
                                    <a class="nav-link" href="/listausuarios">Ver Usuarios</a>
                                    <a class="nav-link" href="/registarusuario">Registrar Usuarios</a>
                                </nav>
                            </div>

                            <!-- Opciones Semáforos Administrador-->
                            <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseSemAdm" aria-expanded="false" aria-controls="collapseLayouts">
                              <div class="nav-link-icon"><i class="material-icons">build</i></div>
                                Configuración Semáforos
                                <div class="drawer-collapse-arrow"><i class="material-icons">expand_more</i></div>
                            </a>
                            <!-- Subopciones SemAdm -->
                            <div class="collapse" id="collapseSemAdm" aria-labelledby="headingOne" data-bs-parent="#drawerAccordion">
                                <nav class="drawer-menu-nested nav">
                                    <a class="nav-link" href="/ListaSemaforos">Ver configuración Semáforos</a>
                                    <a class="nav-link" href="/registarsemaforo">Registrar Semáforos</a>
                                </nav>
                            </div>    
                                           
                        </div>
                    </div>
                </nav>
            </div>
            </div>
      <router-view />
    </body>
    </div>
</template>
<script>
import {LoginStore} from '@/store/LoginStore.js'
import { storeToRefs } from 'pinia'


export default {
  name: 'HomeView',
  setup:()=>{
    const log = LoginStore()
    const {Token} = storeToRefs(LoginStore)
    
  }
}
</script>


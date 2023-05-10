<template>
    <div id="app">
      <!-- Barra de navegacion  -->
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <router-link class="navbar-brand" to="/">Sistema de Control</router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link class="nav-link" to="/">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/Semaforo">Control de Semaforos</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/login">Inisar Secion</router-link>
              </li>
              <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Administracion Usarios
          </a>
          <ul class="dropdown-menu">
            <li><router-link class="dropdown-item" to="/listausuarios">Ver</router-link></li>
            <li><router-link class="dropdown-item" to="/registarusuario">Registar</router-link></li>
          </ul>
        </li>

       <!----> 
       <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Afministracion Semeaforo
          </a>
          <ul class="dropdown-menu">
            <li><router-link class="dropdown-item" to="/ListaSemaforos">Ver</router-link></li>
            <li><router-link class="dropdown-item" to="/registarsemaforo">Reguistar</router-link></li>
          </ul>
        </li>


            </ul>
          </div>
        </div>
      </nav>

      <!-- Contenido de la app web  -->
      <router-view />

    </div>
</template>


<template>
SemaforoNuevaVista
    <div id="app">
        <div class="container mt-4">

          <div class="col">
            <h2>Añadir un Semáforo o un nodo</h2><br>
            </div>
            
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label">Nombre del Semáforo o del Nodo</label>
                  <input  type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <button  class="btn btn-outline-secondary">Cancelar</button>
                <a href="/ListaSemaforos" v-on:click="sumit" class="btn btn-success m-3" data-toggle="tooltip" data-placement="top" 
                title="Recuerda que la dirección IP  del semáforo se registra al inciar la Raspberry.">Registrar</a>
    <div>
        <div class="container mt-4">

          <div class="col">
            <h2>Añadir un Usuario</h2><br>
            </div>
            
                <div class="col-xs-4 mb-3">
                  <label for="exampleInputEmail1" class="form-label">Nombre o Usuario</label>
                  <input  type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <div class="col-xs-4 mb-3">
                  <label for="exampleInputEmail1" class="form-label">No. de Ficha</label>
                  <input  type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <div class="col-xs-4 mb-3">
                  <label for="exampleInputPassword1" class="form-label">Contraseña</label>
                  <input type="password" v-model="Contraseña" class="form-control" id="exampleInputPassword1">
                </div>
                <div class="col-xs-4 mb-4">
                  <label for="exampleInputPassword1" class="form-label">Confimar Contraseña</label>
                  <input type="password" v-model="Contraseña" class="form-control" id="exampleInputPassword1">
                </div>
                
                <div class="dropdown mb-3">
                  <button class="btn btn-dark dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Selecciona un rol
                  </button>
                  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <a class="dropdown-item" href="#">Administrador</a>
                    <a class="dropdown-item" href="#">Operador</a>
                    <a class="dropdown-item" href="#">Visitante</a>
                  </div>
                </div>

                <button  class="btn btn-outline-secondary">Cancelar</button>
                <a href="Usarios.html" v-on:click="sumit" class="btn btn-success m-3">Crear Usuario</a>
main
              
        </div>
    </div>
</template>
<script>
export default{
    data() {
      return {
      
      }
    },
    methods:{
        
    }
  }
</script>
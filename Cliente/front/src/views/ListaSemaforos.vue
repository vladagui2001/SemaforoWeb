<template>
    <div id="app">
        <div class="container">
            <div class="container mt-3">
        <div class="row">
          <div class="col">
            <h1>Administración de Semáforos</h1><br>
            <h3>Buscar Semáforo:</h3><br>
          </div>
          
          <div class="container">
            <div class="row">
              <div class="col"><input  type="text" class="form-control" placeholder="Ingresa un ID..."></div>
              <div class="col"><input  type="text" class="form-control" placeholder="Ingresa un Semáforo o Nodo..."></div>
              <div class="col"><input  type="text" class="form-control" placeholder="Ingresa una Dirección IP..."></div>
              <div class="col"><button class="btn btn-dark">Buscar</button></div>
              <div class="col"><router-link to="/registarsemaforo" class="btn btn-success">Agregar Nuevo Semáforo</router-link></div>
            </div>
            </div>
            
        <div class="bd-example">
          <table class="table mt-4">
            <thead class="table-dark">
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Nombre Nodo</th>
                <th scope="col">Dirección IP</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(Semaforo) in Semaforos">
                <td scope="col">{{Semaforo.ID}}</td>
                <td scope="col">{{Semaforo.NOMBRE}}</td>
                <td scope="col">{{Semaforo.IP}}</td>
                <td><div class="col mr-3">
                  <button class="btn btn-outline-secondary">Modificar</button>
                  <button class="btn btn-outline-secondary m-2">Eliminar</button>
              </div></td>
              </tr>
            </tbody>
          </table> 
        </div>     
              </div>
            </div>
          </div>
        </div>
</template>
<script>
export default{
    data() {
      return {
       Semaforos:[]
      }
    },
    created(){
      this.$http.get('http://127.0.0.1:7000/Semaforos')
                    .then(res=>{
                     this.Semaforos= res.data
                    })
      
    },
    methods:{
      
        
    }
  }
</script>
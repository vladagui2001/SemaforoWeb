<template>
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
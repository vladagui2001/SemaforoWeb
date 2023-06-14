<template>
    <div id="app">
        <div class="container">
            <div class="container mt-3">
        <div class="row">
          <div class="col">
            <h1 class="unselectable">ㅤ</h1><br>
            <h1 class="unselectable">Administración de Semáforos</h1><br>
          </div>
          
          <div class="container">
            <div class="row">
              <div class="col"><router-link to="/registarsemaforo" class="btn btn-success">Agregar Nuevo Semáforo</router-link></div>
            </div>
            </div>
            
        <div class="bd-example">
          <table class="table mt-4">
            <thead class="table-dark">
              <tr>
                <th scope="col" class="unselectable">ID</th>
                <th scope="col" class="unselectable">Nombre Nodo</th>
                <th scope="col" class="unselectable">Dirección IP</th>
                <th scope="col" class="unselectable"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(Semaforo) in Semaforos">
                <td scope="col">{{Semaforo.ID}}</td>
                <td scope="col">{{Semaforo.NOMBRE}}</td>
                <td scope="col">{{Semaforo.IP}}</td>
                <td><div class="col mr-3">
                  <button class="btn btn-outline-secondary" v-on:click="Modificar()">Modificar</button>
                  <button class="btn btn-outline-secondary m-2" v-on:click="eliminar(Semaforo.ID)">Eliminar</button>
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
      eliminar(id){
        this.$swal.fire({
          title: '¿Estás seguro que quieres eliminar el registro?',
          text: "Una vez eliminado no se podrá recuperar",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Sí, Eliminar',
          cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
              this.$http.post('http://127.0.0.1:7000/Semaforo/Delete/'+id).then(res=>{
                this.$swal.fire(
                'Reguistro a sido Eliminado!',
                'El reguistro a sido eliminado permante mente',
                'Corectamnte '
              ).then(()=>{
                window.location.reload()
              })

              })
            }
          })
      },
      Modificar(){
        alert('Presionaste Modificar')
      }
      
        
    }
  }
</script>
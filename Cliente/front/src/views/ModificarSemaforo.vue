<template>
    <div>
        <div class="container mt-4">

          <div class="col">
            <h2>Añadir un Semáforo o un nodo</h2><br>
            </div>
            
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label">Id del Semáforo o del Nodo</label>
                  <label>{{ Id }}</label>
                </div>
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label">Nombre del Semáforo o del Nodo</label>
                  <input v-model="Nombre"  type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label">Ip del Semáforo o del Nodo</label>
                  <input v-model="Ip"  type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <button v-on:click="enviar()"  class="btn btn-outline-secondary">Reguistar</button>
                <router-link to="/listasemaforos"  class="btn btn-success m-3" data-toggle="tooltip" data-placement="top" 
                title="Recuerda que la dirección IP del semáforo se registra al inciar la Raspberry.">Cancelar</router-link>
              
        </div>
    </div>
</template>
<script>
export default{
    name:"ModificarSemaforo",
    props: ['id'],
    data() {
      return {
        Id:"",
        Nombre:"",
        Ip:""
      }
    },
    created(){
      console.log(this.$route.params.id);
      this.$http.get('http://127.0.0.1:7000/Semaforos/'+this.$route.params.id)
                    .then(res=>{
                     this.Id= this.$route.params.id
                     this.Nombre= res.data[0].NOMBRE
                     this.Ip= res.data[0].IP
                    })
      
    },
    methods:{
      /*
      enviar(){
        let Nombre = this.Nombre
        this.$http.post('http://127.0.0.1:7000/Semaforos/Edit',
        {
          Nombre
        })
        this.$router.push("ListaSemaforos");
      }*/
      
        
    }
}

</script>
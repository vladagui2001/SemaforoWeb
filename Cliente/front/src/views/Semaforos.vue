<template>
    <div>
        
        <div class="container mb-0">
            <!-- parte 1 -->
            <div class="raw">
                <div class="unselectable col"></div>
                <div class="unselectable col"></div>
                <div class="unselectable col"></div>
            </div>
            <!-- parte 1 -->
            <div class="container mt-3">
                <div class="col">
                  <h1>ㅤ</h1><br>
                  <h1 class="unselectable">Semáforos en Funcionamiento</h1>
                </div>
                <div class="col">
                    <table class="table mt-5">
            <thead class="table-dark">
              <tr>
                <th scope="col" class="unselectable">ID</th>
                <th scope="col" class="unselectable">Nombre Nodo</th>
                <th scope="col" class="unselectable">Dirección IP</th>
                <th scope="col" class="unselectable">Estado del Semáforo</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(Semaforo) in Semaforos">
                <td scope="col">{{Semaforo.ID}}</td>
                <td scope="col">{{Semaforo.NOMBRE}}</td>
                <td scope="col">{{Semaforo.IP}}</td>
                <td><div class="col mr-3">
                  <button class="btn btn-success" v-on:click="EsradoA">Encender</button>
                  <button class="btn btn-danger m-2" v-on:click="EsradoB">Apagar</button>
              </div></td>
              </tr>
            </tbody>
          </table> 
                </div>     
                <div class="col"></div>
            </div>
           

        </div>
    </div>
</template>
<script>

export default{
    name:'Semaforos',
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
        EsradoA(){
            this.$http.get('http://127.0.0.1:7000/Control/A/1')
                    .then(res=>{
                      
                     alert(res.data) 
                    })
        },
        EsradoB(){
            this.$http.get('http://127.0.0.1:7000/Control/B/1')
                    .then(res=>{
                      
                     alert(res.data.men) 
                    })
        }
    }
}

</script>
<template>
    <div class="mt-5">
        <div class="container">
  <div class="row">
    <div class="col">
      <label >{{ PIdUnico }}</label>
    </div>
    <div class="col">
      <label >{{ PNombre }}</label>
    </div>
    <div class="col">
      <label v-if="PEstado == false">Rojo</label>
      <label v-else>Verde</label>
    </div>
    <div class="col">
      <button class="btn btn-success">Encender Luz Verde</button>
    </div>
    <div class="col">
        <button class="btn btn-danger">Encender Luz Roja</button>
    </div>
    <div class="col">
      <label>IP {{ PDirecionIp }}</label>
    </div>
    <div class="col">
        <router-link to="/configuracion"  class="btn btn-primary">Ajustes</router-link>
    </div>
  </div>
</div>
    </div>
</template>

<script>
export default {
  methods:{
    
  },
  //name:'InformacionSemaforo',
    data: function () {
        return {
          /**Nombre:PNombre,
          DirecionIp:"172.16.255.254",
          IdUnico:1,
          Estado:true*/
            
        }
    },
    props: {
      PNombre:String,
      PDirecionIp:String,
      PIdUnico:Number,
      PEstado:Boolean
      
  }
}
</script>
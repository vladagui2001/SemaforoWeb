<template>

    <div>
        <div class="container mt-4">

          <div class="col">
            <h2>ㅤ</h2><br>
            <h2>Añadir un Usuario</h2><br>
            </div>
            
                <div class="col-xs-4 mb-3 form-outline w-50">
                  <label for="exampleInputEmail1" class="form-label">Nombre o Usuario</label>
                  <input  type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <div class="col-xs-4 mb-3 form-outline w-50">
                  <label for="exampleInputEmail1" class="form-label">No. de Ficha</label>
                  <input  type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <div class="col-xs-4 mb-3 form-outline w-50">
                  <label for="exampleInputPassword1" class="form-label">Contraseña</label>
                  <input type="password" v-model="Contraseña" class="form-control" id="exampleInputPassword1">
                </div>
                <div class="col-xs-4 mb-4 form-outline w-50">
                  <label for="exampleInputPassword1" class="form-label">Confimar Contraseña</label>
                  <input type="password" v-model="Contraseña" class="form-control" id="exampleInputPassword1">
                </div>
                
                <div class="dropdown mb-3">
                  <label class="form-label">Selecciona un rol:</label>
                  <select class="form-select mb-3 form-outline w-25">
                        <option value="Administrador">Administrador</option>
                        <option value="Operador">Operador</option>
                        <option value="Visitante">Visitante</option>
                  </select>
                </div>

                <button v-on:click="enviar()" class="btn btn-success">Crear Usuario</button>
                <router-link to="/listausuarios"  v-on:click="sumit" class="btn btn-outline-secondary m-3">Cancelar</router-link>

              
        </div>
    </div>
</template>
<script>
export default{
    name:"RegistarUsuario",
    data() {
      return {
        Nombre:""
      }
    },
    
    methods:{
      enviar(){
        let Nombre = this.Nombre
        this.$http.post('http://127.0.0.1:7000/Usarios/Add',
        {
          Nombre
        })
        this.$router.push("ListaUsuarios");
        location.reload()
      }
      
        
    }
}

</script>
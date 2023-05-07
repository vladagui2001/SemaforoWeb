<template>
    <div>
        <div class="container">
            
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label">Usuario</label>
                  <input v-model="Usuario" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                  <label for="exampleInputPassword1" class="form-label">Contraseña</label>
                  <input type="password" v-model="Contraseña" class="form-control" id="exampleInputPassword1">
                </div>
                <button v-on:click="sumit()" class="btn btn-primary">Iniciar Sesión</button>
              
        </div>
    </div>
</template>
<script>
import { logicalExpression } from '@babel/types';

export default{
    name:"LogIn",
    data() {
      return {
        Usuario:"",
        Contraseña:""
      }
    },
    methods:{
        sumit(){
            let username=this.Usuario
            let password=this.Contraseña
            console.log({
            username,
            password

        });
        
          
        this.$http.post("http://127.0.0.1:7000/login",
        {
            username,
            password

        }
        ).then(function (response) {
        
        console.log(response)
          
        });

        
        }
    }
}
</script>
<style>
</style>
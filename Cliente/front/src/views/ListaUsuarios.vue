<template>

<div class="container">
    
    <div class="container mt-3">
        <div class="row">
          <div class="col">
            <h1></h1><br>
            <h1>Administración de Usuarios</h1><br>
            <h3>Buscar Usuario:</h3><br>
          </div>
          
          <div class="container">
            <div class="row">
              <div class="col"><input  type="text" class="form-control" placeholder="Ingresa un ID..."></div>
              <div class="col"><input  type="text" class="form-control" placeholder="Ingresa un Nombre..."></div>
              <div class="col"><input  type="text" class="form-control" placeholder="Ingresa un Folio..."></div>
              <div class="col"><input  type="text" class="form-control" placeholder="Ingresa un Rol..."></div>
              <div class="col"><button class="btn btn-dark">Buscar</button></div>
              <div class="col"><router-link to="/registarusuario" href="AddUsuario.html" class="btn btn-success">Agregar Nuevo Usuario</router-link></div>
            </div>
            </div>
            
        <div class="bd-example">
          <table class="table mt-4">
            <thead class="table-dark">
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Nombre/Usuario</th>
                <th scope="col">Ficha</th>
                <th scope="col">Rol</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>

              <tr v-for="(Usuario) in Usuarios">
                <td scope="col">{{Usuario.ID}}</td>
                <td scope="col">{{Usuario.Usuario}}</td>
                <td scope="col">{{Usuario.FICHA}}</td>
                <td scope="col">{{Usuario.Permiso}}</td>


      
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
</template>
<script>
import { logicalExpression } from '@babel/types';
export default {
        data() {
          return {
           Usuarios:[]
          }
        },
        methods:{
            
        },
        created(){
      this.$http.get('http://127.0.0.1:7000/Usarios')
                    .then(res=>{
                      
                     this.Usuarios= res.data
                    })
      
    }
  }
</script>
<template>

<div class="container">
    
    <div class="container mt-3">
        <div class="row">
          <div class="col">
            <h1 class="unselectable"></h1><br>
            <h1 class="unselectable">ㅤ</h1><br>
            <h1 class="unselectable">Administración de Usuarios</h1><br>
          </div>
          
          <div class="container">
            <div class="row">
              <div class="col"><router-link to="/registarusuario" href="AddUsuario.html" class="btn btn-success">Agregar Nuevo Usuario</router-link></div>
            </div>
            </div>
            
        <div class="bd-example">
          <table class="table mt-4">
            <thead class="table-dark">
              <tr>
                <th scope="col" class="unselectable">ID</th>
                <th scope="col" class="unselectable">Nombre/Usuario</th>
                <th scope="col" class="unselectable">Ficha</th>
                <th scope="col" class="unselectable">Rol</th>
                <th scope="col" class="unselectable"></th>
              </tr>
            </thead>
            <tbody>

              <tr v-for="(Usuario) in Usuarios">
                <td scope="col">{{Usuario.ID}}</td>
                <td scope="col">{{Usuario.Usuario}}</td>
                <td scope="col">{{Usuario.FICHA}}</td>
                <td scope="col">{{Usuario.Permiso}}</td>


      
                <td><div class="col mr-3">
                  <button class="btn btn-outline-secondary" v-on:click="Modificar()">Modificar</button>
                  <button class="btn btn-outline-secondary m-2" v-on:click="eliminar(Usuario.ID)">Eliminar</button>
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
          eliminar(id){
        this.$swal.fire({
          title: '¿quieres Eliminaras Este Reguistro Pra Simpre?',
          text: "¿Estas Seguro?",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
              this.$http.post('http://127.0.0.1:7000/Usarios/Delete/'+id).then(res=>{
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
      
            
        },
        created(){
      this.$http.get('http://127.0.0.1:7000/Usarios')
                    .then(res=>{
                      
                     this.Usuarios= res.data
                    })
      
    }
  }
</script>
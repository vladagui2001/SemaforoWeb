<template>

<div class="container">
    
    <div class="container mt-3">
        <div class="row">
          <div class="col">
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
              <tr>
                <td scope="col">{{Usuarios[0].ID}}</td>
                <td scope="col">{{Usuarios[0].NOMBRE}}</td>
                <td scope="col">{{Usuarios[0].FICHA}}</td>
                <td scope="col">{{Usuarios[0].ROL}}</td>
                <td><div class="col mr-3">
                  <button class="btn btn-outline-secondary">Modificar</button>
                  <button class="btn btn-outline-secondary m-2">Eliminar</button>
              </div></td>
              </tr>

              <tr>
                <td scope="col">{{Usuarios[1].ID}}</td>
                <td scope="col">{{Usuarios[1].NOMBRE}}</td>
                <td scope="col">{{Usuarios[1].FICHA}}</td>
                <td scope="col">{{Usuarios[1].ROL}}</td>
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
           Usuarios:[
            {   
                ID:1,
                NOMBRE:"Ejemplo",
                FICHA:"Ejemplo",
                ROL:"Ejemplo"
            },
            {   
                ID:2,
                NOMBRE:"Ejemplo 2",
                FICHA:"Ejemplo 2",
                ROL:"Ejemplo 2"
            }
           ]
          }
        },
        methods:{
            
        }
      }
</script>
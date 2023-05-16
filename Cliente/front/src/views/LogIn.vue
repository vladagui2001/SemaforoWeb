<template>
    <div>
      <body class="bg-pattern-mina">
        <!-- Layout wrapper-->
        <div id="layoutAuthentication">
            <!-- Layout content-->
            <div id="layoutAuthentication_content">
                <!-- Main page content-->
                <main>
                    <!-- Main content container-->
                    <div class="container">
                        <div class="row justify-content-center">
                            <div class="col-xxl-10 col-xl-10 col-lg-12">
                                <div class="card card-raised shadow-10 mt-5 mt-xl-10 mb-4">
                                    <div class="row g-0">
                                        <div class="col-lg-5 col-md-6">
                                            <div class="card-body p-5">
                                                <!-- Auth header with logo image-->
                                                <div class="text-center">
                                                    <img class="mb-3" src="@/assets/Material/assets/img/icons/background.svg" alt="..." style="height: 48px" />
                                                    <h1 class="display-5 mb-0">Control Semáforos</h1>
                                                    <div class="subheading-1 mt-3 mb-5">Por favor inicie sesión</div>
                                                </div>
                                                <!-- Login submission form-->
                                                <form class="mb-5">
                                                    <div class="mb-4"><mwc-textfield class="w-100" label="Usuario/Folio" outlined></mwc-textfield></div>
                                                    <div class="mb-4"><mwc-textfield class="w-100" label="Contraseña" outlined icontrailing="visibility_off" type="password"></mwc-textfield></div>
                                                    <div class="form-group d-flex align-items-center justify-content-center">
                                                        <a class="btn btn-dark" href="/Semaforo">Iniciar Sesión</a>
                                                    </div>
                                                </form>
                                                <!-- Auth card message-->                                            </div>
                                        </div>
                                        <!-- Background image column using inline CSS-->
                                        <div class="col-lg-7 col-md-6 d-none d-md-block">
                                            <img class="mt-6" src="@/assets/Material/assets/img/sem1.jpg" width="510" height="530" style="background-size: cover; background-repeat: no-repeat; background-position: center"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
            <!-- Layout footer-->
            <div id="layoutAuthentication_footer"></div>
        </div>
    </body>
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
<template>
    <div>
        <form class="container mt-5">
                <div class="col ">
                    <h1 class="text-center">ㅤ</h1>
                    <h1>Configuración De Modo</h1>
                    <div class="container">
                        <div class="col-xs-4 mb-4">
                            <div class="col">{{ Id }}</div>
                            <div class="col">{{ Ip }}</div>
                            <div class="col">{{ Nombre }}</div>
                        </div>
                    </div>
                    <label>Modo De Configuración</label>
                    <select class="form-select mb-3 form-outline w-25">
                        <option value="Manual">Manual</option>
                        <option value="Automatico DataSet">Automático DataSet</option>
                        <option value="Automatico Sensor">Automático Sensor</option>
                    </select>
                    <div class="form-outline w-25">
                        <label>Data Set</label>
                        <input type="number" class="input-group mb-3">
                    </div>
                    <button class="btn btn-success">Registar</button>
                <router-link to="/Semaforo"  class="btn btn-outline-secondary m-3" data-toggle="tooltip" data-placement="top">Cancelar</router-link>
                </div>
        </form>
    </div>
</template>

<script>
export default{
    
}
</script>
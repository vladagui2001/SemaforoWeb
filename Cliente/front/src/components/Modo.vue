<template>
    <div>
        <form class="container">
            <div class="row">
                <div class="col-3">
                    <h1 class="text-center">Configuracion De Modo</h1>
                    <div class="container">
                        <div class="row">
                            <div class="col">{{ Id }}</div>
                            <div class="col">{{ Ip }}</div>
                            <div class="col">{{ Nombre }}</div>
                        </div>
                    </div>
                    <label>Modo De Configuracion</label>
                    <select class="form-select mb-3">
                        <option value="Manual">Manual</option>
                        <option value="Automatico DataSet">Automatico DataSet</option>
                        <option value="Automatico Sensor">Automatico Sensor</option>
                    </select>
                    <div>
                        <label>Data Set</label>
                        <input type="number" class="input-group mb-3">
                    </div>
                    <button type="button" class="btn btn-primary">Enbiar</button>
                    <button type="button" class="btn btn-secondary">Canselar</button>
                </div>
                
            </div>
        </form>
    </div>
</template>
<script>
export default{
    data:function(){
        return{
            "Id":"8",
            "Ip":"192.168.1.65",
            "Nombre":"Rampa Norte 12"
        }
    }
}
</script>
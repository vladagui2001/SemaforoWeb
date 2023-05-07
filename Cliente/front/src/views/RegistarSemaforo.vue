<template>
    <div>
        <form class="container">
            <div>
                <label>Nombre Del Semaforo</label>
                <input type="text"  class="input-group mb-3">
            </div>
            <div>
                <label>Direccion ip (Parcial)</label>
                <input type="text"  class="input-group mb-3">
            </div>
            <div>
                <label class="mb-3">Permisos del Nodo</label>
                <div class="input-group">
                    <div class="input-group-text">
                        <input class="form-check-input mt-0" type="radio" value="" aria-label="Radio button for following text input">
                    </div>
                   <label class="ms-3">Modificar Configracion</label>
                </div>
                <div class="input-group">
                    <div class="input-group-text">
                        <input class="form-check-input mt-0" type="radio" value="" aria-label="Radio button for following text input">
                    </div>
                   <label class="ms-3">Modo Manual</label>
                </div>
                <div class="input-group">
                    <div class="input-group-text">
                        <input class="form-check-input mt-0" type="radio" value="" aria-label="Radio button for following text input">
                    </div>
                   <label class="ms-3">Modo Automatico Sensor</label>
                </div>
                <div class="input-group">
                    <div class="input-group-text">
                        <input class="form-check-input mt-0" type="radio" value="" aria-label="Radio button for following text input">
                    </div>
                   <label class="ms-3">Modo Automatico DataSet</label>
                </div>
            </div>
            <div>
                <button class="btn btn-primary mt-3">Guardar</button>
                <button class="btn btn-danger mt-3 ms-2">Canselar</button>
            </div>
        </form>
    </div>
</template>
<script>

</script>
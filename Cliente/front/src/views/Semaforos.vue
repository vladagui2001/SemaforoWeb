<template>
    <div>
        <div class="container mt-5">
            <!-- parte 1 -->
            <div class="raw">
                <div class="col"></div>
                <div class="col"></div>
                <div class="col"></div>
            </div>
            <!-- parte 1 -->
            <div class="raw">
                <div class="col"></div>
                <div class="col">
                    <HeasInformacionSemaforo></HeasInformacionSemaforo>
                    <InformacionSemaforo 
                    p-nombre="Rampa 2 -12"
                    p-direcion-ip="182.169.1.2"
                    p-id-unico="1"
                    p-estado="true"
                    ></InformacionSemaforo>

                    <InformacionSemaforo 
                    p-nombre="Rampa norte 1-13"
                    p-direcion-ip="182.169.1.7"
                    p-id-unico="2"
                    p-estado="true"
                    ></InformacionSemaforo>

                </div>
                <div class="col"></div>
            </div>
           

        </div>
    </div>
</template>
<script>
import InformacionSemaforo from '@/components/InformacionSemaforo.vue';
import HeasInformacionSemaforo from '@/components/HeadInformacionSemaforo.vue';

export default{
    name:'Semaforos',
    components:{
        InformacionSemaforo,
        HeasInformacionSemaforo
    }
}

</script>
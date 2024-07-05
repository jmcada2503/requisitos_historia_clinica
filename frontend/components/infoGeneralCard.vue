<template>
    <v-container
    fluid
    class="d-flex align-center"
    style="border-radius:20px;height:250px;"
    :style="!closed ? 'background-color:#DDD' : 'background-color:white;border: 2px solid #fca2a2'"
    @click="info_detallada()"
    >
        <v-row>
            <v-col
            cols=6
            class="d-flex align-center"
            >
                <v-row
                class="d-flex justify-center"
                >
                    <span
                    class="font-weight-bold"
                    style="font-size:24px;text-align:center;"
                    >
                        {{ nombre }}
                    </span>
                </v-row>

                <v-divider
                vertical
                />
            </v-col>


            <v-col
            cols=6
            >
                <v-row
                class="d-flex justify-center pa-5"
                >
                    <span
                    class="font-weight-bold"
                    >
                        Descripción:&nbsp;
                        <span
                        style="font-weight:normal;"
                        >
                            {{ descripcion }}
                        </span>
                    </span>
                </v-row>

                <v-divider
                class="my-5"
                />

                <v-row
                class="pa-5"
                >
                    <span
                    class="font-weight-bold"
                    >
                        {{ nombre_caracteristicas }}:&nbsp;
                        <span
                        style="font-weight:normal;"
                        >
                            {{ caracteristicas }}
                        </span>
                    </span>

                </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: "info_general_card",
    props: [
        "id",
        "id_paciente",
        "nombre",
        "caracteristicas",
        "descripcion",
        "nombre_caracteristicas",
        "closed",
    ],
    methods: {
        info_detallada() {
            if (this.nombre_caracteristicas == "Síntomas") {
                this.$router.push(`/problema_clinico?id=${this.id}&id_paciente=${this.id_paciente}`)
            }
            else if (this.nombre_caracteristicas == "Razones") {
                this.$router.push(`/factor_riesgo?id=${this.id}&id_paciente=${this.id_paciente}`)
            }
        }
    }
}
</script>

<style scoped>
    .container:hover {
        cursor: pointer !important;
    }
</style>

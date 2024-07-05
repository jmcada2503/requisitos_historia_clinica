<template>
    <v-container
    fluid
    >
        <v-row>
            <v-col
            cols=12
            class="d-flex justify-center py-10"
            style="background-color:#5DB1F1"
            >
                <span
                class="font-weight-bold"
                style="color:white;font-size:40px;"
                >
                    Módulo de gestión de problemas clínicos y factores de riesgo
                </span>
            </v-col>
        </v-row>

        <v-row>
            <v-col
            cols=12
            class="d-flex justify-center"
            >
                <span
                class="font-weight-bold"
                style="color:#BBB;font-size:22px;"
                >
                    Presione un recuadro para ver más información
                </span>
            </v-col>
        </v-row>

        <v-row
        class="mt-10"
        >
            <v-col
            cols=6
            class="px-16"
            >
                <v-row
                class="d-flex justify-center mb-5"
                >
                    <span
                    class="font-weight-bold"
                    style="color:#5DB1F1;font-size:40px;"
                    >
                        Problemas Clínicos
                    </span>
                </v-row>

                <v-row
                v-for="info in problemas_clinicos.abiertos"
                :key="info.id"
                class="my-5"
                v-show="!loading"
                >
                    <info-general-card
                    :id="info.id"
                    :id_paciente="info.id_paciente"
                    :nombre="info.problema_clinico.nombre"
                    :descripcion="info.problema_clinico.descripcion"
                    :caracteristicas="info.problema_clinico.sintomas"
                    :closed="false"
                    nombre_caracteristicas="Síntomas"
                    />
                </v-row>

                <v-row
                v-for="info in problemas_clinicos.cerrados"
                :key="info.id"
                class="my-5"
                v-show="!loading && problemas_clinicos.show_closed"
                >
                    <info-general-card
                    :id="info.id"
                    :id_paciente="info.id_paciente"
                    :nombre="info.problema_clinico.nombre"
                    :descripcion="info.problema_clinico.descripcion"
                    :caracteristicas="info.problema_clinico.sintomas"
                    :closed="true"
                    nombre_caracteristicas="Síntomas"
                    />
                </v-row>

                <v-row
                v-for="index in 2"
                :key="index"
                class="my-5"
                v-show="loading"
                >
                    <v-skeleton-loader
                    type="image"
                    class="ma-0 pa-0"
                    height="250px"
                    width="100%"
                    style="border-radius:20px;"
                    />
                </v-row>

                <v-row>
                    <v-col
                    cols=2
                    />
                    <v-col
                    cols=8
                    class="d-flex justify-space-around"
                    >
                        <v-btn
                        rounded
                        dark
                        color="#5DB1F1"
                        class="py-6 px-10"
                        style="text-transform:none;"
                        @click="problemas_clinicos.show_closed = !problemas_clinicos.show_closed"
                        >
                            <span
                            class="font-weight-bold"
                            style="font-size:24px;"
                            v-if="!problemas_clinicos.show_closed"
                            >
                                Ver cerrados
                            </span>

                            <span
                            class="font-weight-bold"
                            style="font-size:24px;"
                            v-if="problemas_clinicos.show_closed"
                            >
                                Ocultar cerrados
                            </span>
                        </v-btn>

                        <v-btn
                        rounded
                        dark
                        color="#5DB1F1"
                        class="py-6 px-10"
                        style="text-transform:none;"
                        @click="$router.push(`/agregar_problema?id_paciente=${$route.query.id_paciente}`)"
                        >
                            <span
                            class="font-weight-bold"
                            style="font-size:24px;"
                            >
                                Agregar
                            </span>
                        </v-btn>
                    </v-col>
                </v-row>
            </v-col>

            <v-col
            cols=6
            class="px-16"
            >
                <v-row
                class="d-flex justify-center mb-5"
                >
                    <span
                    class="font-weight-bold"
                    style="color:#5DB1F1;font-size:40px;"
                    >
                        Factores de Riesgo
                    </span>
                </v-row>

                <v-row
                v-for="info in factores_riesgo.abiertos"
                :key="info.id"
                class="my-5"
                v-show="!loading"
                >
                    <info-general-card
                    :id="info.id"
                    :id_paciente="info.id_paciente"
                    :nombre="info.factor_riesgo.nombre"
                    :descripcion="info.factor_riesgo.descripcion"
                    :caracteristicas="info.factor_riesgo.razones"
                    nombre_caracteristicas="Razones"
                    />
                </v-row>

                <v-row
                v-for="info in factores_riesgo.cerrados"
                :key="info.id"
                class="my-5"
                v-show="!loading && factores_riesgo.show_closed"
                >
                    <info-general-card
                    :id="info.id"
                    :id_paciente="info.id_paciente"
                    :nombre="info.factor_riesgo.nombre"
                    :descripcion="info.factor_riesgo.descripcion"
                    :caracteristicas="info.factor_riesgo.razones"
                    :closed="true"
                    nombre_caracteristicas="Razones"
                    />
                </v-row>

                <v-row
                v-for="index in 1"
                :key="index"
                class="my-5"
                v-show="loading"
                >
                    <v-skeleton-loader
                    type="image"
                    class="ma-0 pa-0"
                    height="250px"
                    width="100%"
                    style="border-radius:20px;"
                    />
                </v-row>

                <v-row>
                    <v-col
                    cols=2
                    />
                    <v-col
                    cols=8
                    class="d-flex justify-space-around"
                    >
                        <v-btn
                        rounded
                        dark
                        color="#5DB1F1"
                        class="py-6 px-10"
                        style="text-transform:none;"
                        @click="factores_riesgo.show_closed = !factores_riesgo.show_closed"
                        >
                            <span
                            class="font-weight-bold"
                            style="font-size:24px;"
                            v-if="!factores_riesgo.show_closed"
                            >
                                Ver cerrados
                            </span>

                            <span
                            class="font-weight-bold"
                            style="font-size:24px;"
                            v-if="factores_riesgo.show_closed"
                            >
                                Ocultar cerrados
                            </span>
                        </v-btn>

                        <v-btn
                        rounded
                        dark
                        color="#5DB1F1"
                        class="py-6 px-10"
                        style="text-transform:none;"
                        @click="$router.push(`/agregar_factor_riesgo?id_paciente=${$route.query.id_paciente}`)"
                        >
                            <span
                            class="font-weight-bold"
                            style="font-size:24px;"
                            >
                                Agregar
                            </span>
                        </v-btn>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: 'paciente',
    data() {
        return {
            problemas_clinicos: {
                abiertos: [],
                cerrados: [],
                show_closed: false
            },
            factores_riesgo: {
                abiertos: [],
                cerrados: [],
                show_closed: false
            },
            loading: true,
        }
    },
    mounted() {
        console.log(this.$route.query.id_paciente)
        if (this.$route.query.id_paciente) {
            this.problemas_clinicos.abiertos = [];
            this.factores_riesgo.abiertos = [];

            this.loading = true;

            let l = [true, true];

            this.$axios.get(`/problemas_clinicos_paciente?id_paciente=${this.$route.query.id_paciente}`)
            .then((response) => {
                for (let i=0; i<response.data.length; i++) {
                    this.problemas_clinicos.abiertos.push(response.data[i]);
                }
            })
            .finally(() => {
                l[0] = false;
                this.loading = l[0] || l[1];
            })

            this.$axios.get(`/factores_riesgo_paciente?id_paciente=${this.$route.query.id_paciente}`)
            .then((response) => {
                for (let i=0; i<response.data.length; i++) {
                    this.factores_riesgo.abiertos.push(response.data[i]);
                }
            })
            .finally(() => {
                l[1] = false;
                this.loading = l[0] || l[1];
            })

            this.$axios.get(`/problemas_clinicos_cerrados_paciente?id_paciente=${this.$route.query.id_paciente}`)
            .then((response) => {
                for (let i=0; i<response.data.length; i++) {
                    this.problemas_clinicos.cerrados.push(response.data[i]);
                }
            })

            this.$axios.get(`/factores_riesgo_cerrados_paciente?id_paciente=${this.$route.query.id_paciente}`)
            .then((response) => {
                for (let i=0; i<response.data.length; i++) {
                    this.factores_riesgo.cerrados.push(response.data[i]);
                }
            })
        }
        else {
            this.$router.push("/");
        }
    }
}
</script>

<style>
    .v-skeleton-loader__image {
        height: 250px;
    }
</style>

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
                    Agregar factor de riesgo
                </span>
            </v-col>
        </v-row>
        
        <v-container
        class="mt-16 pt-16"
        >
            <v-row>
                <v-col
                cols=12
                >
                <span
                class="text-h4"
                >
                    Factor de riesgo
                </span>
                </v-col>
            </v-row>

            <v-row>
                <v-col
                cols=8
                >
                    <v-select
                    outlined
                    hide-details
                    style="width:100%;font-size:24px;"
                    :items="factores_riesgo"
                    v-model="factor_riesgo"
                    />
                </v-col>
            </v-row>
            
            <v-row>
                <v-col
                cols=12
                >
                <span
                class="text-h4"
                >
                    Notas
                </span>
                </v-col>
            </v-row>

            <v-row>
                <v-col
                cols=12
                >
                    <v-textarea
                    outlined
                    hide-details
                    placeholder="Agregar anotaciones acerca del factor de riesgo"
                    style="width:100%;font-size:24px;"
                    v-model="notas"
                    />
                </v-col>
            </v-row>

            <v-row>
                <v-spacer />
                
                <v-col
                cols=6
                class="d-flex justify-space-around mt-10"
                >
                    <v-btn
                    rounded
                    dark
                    color="#5DB1F1"
                    class="py-6 px-10"
                    style="text-transform:none;"
                    @click="crear_factor_riesgo()"
                    >
                        <span
                        class="font-weight-bold"
                        style="font-size:24px;"
                        >
                            Crear
                        </span>
                    </v-btn>

                    <v-btn
                    rounded
                    dark
                    color="#5DB1F1"
                    class="py-6 px-10"
                    style="text-transform:none;"
                    @click="$router.push(`/paciente?id_paciente=${$route.query.id_paciente}`)"
                    >
                        <span
                        class="font-weight-bold"
                        style="font-size:24px;"
                        >
                            Volver
                        </span>
                    </v-btn>
                </v-col>

                <v-spacer />
            </v-row>
        </v-container>
    </v-container>
</template>

<script>
export default {
    name: "agregar_factor_riesgo",
    data() {
        return {
            factor_riesgo: null,
            notas: "",
            factores_riesgo: []
        }
    },
    methods: {
        crear_factor_riesgo() {
            this.$axios.post("/factor_riesgo/", {
                "id_paciente": this.$route.query.id_paciente,
                "factor_riesgo": this.factor_riesgo,
                "notas": this.notas,
            })
            .then(() => {
                this.$router.push(`/paciente/?id_paciente=${this.$route.query.id_paciente}`);
            })
        }
    },
    mounted() {
        if (!this.$route.query.id_paciente) {
            this.$router.push("/");
        }
        this.$axios.get("/factores_riesgo/")
        .then((response) => {
            for (let i=0; i<response.data.length; i++) {
                this.factores_riesgo.push({
                    'text': response.data[i].nombre,
                    'value': response.data[i].id
                })
            }
        })
    }
}
</script>

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
                    Agregar problema clínico
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
                    Problema
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
                    :items="problemas_clinicos"
                    v-model="problema_clinico"
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
                    placeholder="Agregar anotaciones acerca del problema"
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
                    @click="crear_problema()"
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
    name: "agregar_problema",
    data() {
        return {
            problema_clinico: null,
            notas: "",
            problemas_clinicos: []
        }
    },
    methods: {
        crear_problema() {
            this.$axios.post("/problema_clinico/", {
                "id_paciente": this.$route.query.id_paciente,
                "problema_clinico": this.problema_clinico,
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
        this.$axios.get("/problemas_clinicos/")
        .then((response) => {
            for (let i=0; i<response.data.length; i++) {
                this.problemas_clinicos.push({
                    'text': response.data[i].nombre,
                    'value': response.data[i].id
                })
            }
        })
    }
}
</script>

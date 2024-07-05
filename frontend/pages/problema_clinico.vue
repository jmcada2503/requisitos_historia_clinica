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
                    Problema clínico
                </span>
            </v-col>
        </v-row>
        
        <v-container
        class="mt-16"
        >
            <v-row>
                <v-col
                cols=12
                >
                <span
                class="text-h4"
                >
                    Nombre
                </span>
                </v-col>
            </v-row>

            <v-row>
                <v-col
                cols=8
                >
                    <v-text-field
                    outlined
                    hide-details
                    readonly
                    style="width:100%;font-size:24px;"
                    v-model="nombre"
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
                    Descripción
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
                    readonly
                    style="width:100%;font-size:24px;"
                    v-model="descripcion"
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
                    Síntomas
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
                    readonly
                    style="width:100%;font-size:24px;"
                    v-model="sintomas"
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
                    Estado
                </span>
                </v-col>
            </v-row>

            <v-row>
                <v-col
                cols=6
                >
                    <v-select
                    outlined
                    hide-details
                    style="width:100%;font-size:24px;"
                    v-model="estado"
                    :items="estados"
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
                    style="width:100%;font-size:24px;"
                    v-model="notas"
                    />
                </v-col>
            </v-row>

            <v-row
            class="mb-8"
            >
                <v-spacer />
                
                <v-col
                cols=10
                class="d-flex justify-space-around mt-10"
                >
                    <v-btn
                    rounded
                    dark
                    color="#5DB1F1"
                    class="py-6 px-10"
                    style="text-transform:none;"
                    @click="mostrar_historial = !mostrar_historial"
                    >
                        <span
                        class="font-weight-bold"
                        style="font-size:24px;"
                        v-show="!mostrar_historial"
                        >
                            Ver historial de cambios
                        </span>

                        <span
                        class="font-weight-bold"
                        style="font-size:24px;"
                        v-show="mostrar_historial"
                        >
                            Ocultar historial de cambios
                        </span>
                    </v-btn>

                    <v-btn
                    rounded
                    dark
                    color="#5DB1F1"
                    class="py-6 px-10"
                    style="text-transform:none;"
                    @click="editar_problema_clinico()"
                    >
                        <span
                        class="font-weight-bold"
                        style="font-size:24px;"
                        >
                            Guardar
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

            <v-container
            fluid
            v-for="(cambio, index) in cambios"
            :key="index"
            v-show="mostrar_historial"
            >
                <v-row>
                    <v-col
                    cols=12
                    class="pb-0"
                    >
                        <span class="text-h5">Fecha:&nbsp;&nbsp;{{ cambio.fecha.substring(0, 19).replace('T', ' ') }}</span>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col
                    cols=12
                    class="py-0"
                    >
                        <span class="text-h5">Estado:&nbsp;&nbsp;{{ estados.filter((e) => e.value == cambio.estado)[0].text }}</span>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col
                    cols=12
                    class="py-0"
                    >
                        <span class="text-h5">Notas:</span>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col
                    cols=12
                    class="pt-0 pb-10"
                    >
                        <v-textarea
                        outlined
                        hide-details
                        readonly
                        style="width:100%;font-size:22px;"
                        v-model="cambio.notas"
                        />
                        </v-col>
                </v-row>
                <v-divider />
            </v-container>
        </v-container>
    </v-container>
</template>

<script>
export default {
    name: "problema_clinico",
    data() {
        return {
            nombre: "",
            descripcion: "",
            sintomas: "",
            estado: null,
            notas: "",
            mostrar_historial: false,
            cambios: [],
            estados: [
                {
                    "text": "Detectado",
                    "value": "detected"
                },
                {
                    "text": "Abierto",
                    "value": "open"
                },
                {
                    "text": "Editado",
                    "value": "edited"
                },
                {
                    "text": "Cerrado",
                    "value": "closed"
                },
            ],
        }
    },
    methods: {
        editar_problema_clinico() {
            this.$axios.patch("/problema_clinico/", {
                "id": this.$route.query.id,
                "estado": this.estado,
                "notas": this.notas
            })
            .then(() => {
                this.$router.push(`/paciente?id_paciente=${this.$route.query.id_paciente}`);
            })
        },
    },
    mounted() {
        if (!this.$route.query.id) {
            this.$router.push("/");
        }
        this.$axios.get(`/problema_clinico/?id=${this.$route.query.id}`)
        .then((response) => {
            this.nombre = response.data.problema_clinico.nombre;
            this.descripcion = response.data.problema_clinico.descripcion;
            this.sintomas = response.data.problema_clinico.sintomas;
            this.estado = response.data.estado;
            this.notas = response.data.notas;
        })

        this.$axios.get(`/historial_problema_clinico/?id=${this.$route.query.id}`)
        .then((response) => {
            for (let i=response.data.length-1; i>=0; i--) {
                this.cambios.push(response.data[i]);
            }
        })
    }
}
</script>

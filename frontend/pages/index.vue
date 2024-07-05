<template>
  <v-container
  fluid
  class="d-flex align-center justify-center"
  style="height:100%;widht:100%"
  >
    <v-col
    cols=12
    >
        <v-row
        class="d-flex justify-center mb-16"
        >
            <span
            class="text-h2"
            >
            Error: Falta de integración
            </span>
        </v-row>

        <v-row
        class="d-flex justify-center"
        >
            Para consultar los problemas clínicos y factores de riesgo de un paciente
        </v-row>

        <v-row
        class="d-flex justify-center"
        >
            agrega un valor en el parámetro "id_paciente" de la siguiente URL
        </v-row>

        <v-row
        class="d-flex justify-center mt-10"
        >
            <code>
                http://localhost:3000/paciente?id_paciente={id del paciente}
            </code>
        </v-row>
    </v-col>
  </v-container>
</template>

<script>
export default {
    name: 'IndexPage',
}
</script>

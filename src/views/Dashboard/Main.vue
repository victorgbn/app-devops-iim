<template>
    <v-container>
        <h1>Titre</h1>
        <v-btn @click="createAnalyse">
            Action
        </v-btn>
    </v-container>
</template>

<script>
import { API } from '@vue/composition-api'

 export default {
     methods: {
         async createAnalyse() {
             try {
                 console.log('action')
                 await API.post('analyses', '/createAnalyse')
             }
             catch(e) {
                 console.log(e)
             }
         }
     }
    }
</script>

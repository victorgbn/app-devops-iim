<template>
    <v-container>
        <h1>Titre</h1>
        <v-btn @click="createAnalyses">
            Action
        </v-btn>
    </v-container>
</template>

<script>
import { API } from 'aws-amplify'

 export default {
     methods: {
         async createAnalyses() {
             try {
                 console.log('action')
                 await API.post('analyses', '/createAnalyses')
             }
             catch(e) {
                 console.log(e)
             }
         }
     }
    }
</script>

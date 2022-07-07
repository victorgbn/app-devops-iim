<template>
    <v-container>
        <h1>Hello !</h1>
        <v-btn @click="createAnalyses">Create Analyse</v-btn>
    </v-container>
</template>

<script>
import { API } from "aws-amplify";

export default {
  methods: {
    async createAnalyses() {
      try {
        console.log("Create Analyse started");
       const response = await API.post("analyses", "/createAnalyses");
       this.$router.push({ path: `/formAnalyse/:${response.analyseId}` })
      } catch (e) {
        console.log(e);
      }
    },
  },
};
</script>

<template>
  <div style="padding:10rem;">
    <router-link to="/">Back to home</router-link>
    <v-form ref="form" lazy-validation>
      <v-text-field v-model="title" label="Titre" required></v-text-field>

      <v-textarea
        v-model="description"
        label="Description"
        required
      ></v-textarea>
    </v-form>
    <v-btn @click="updateAnalyse">Enregistrer</v-btn>
  </div>
</template>

<script>
import { API } from "aws-amplify";

export default {
  data() {
    return {
      description: this.description,
      title: this.title,
      analyseId: window.location.href.split("/:")[1],
      updated_by: null
    };
  },

  methods: {
    async updateAnalyse() {
      try {

        const options = {
          body: {
            analyse_id: this.analyseId,
            title: this.title,
            description: this.description,
            updatedBy: this.updated_by
          },
        };
        await API.post("analyses", "/updateAnalyse", options).then(
            () => this.$router.push('/')
        );
      } catch (e) {
        console.log(e);
      }
    },

    async getAnalysisById(id) {
      console.log("getAnalysisById started");
      try {
        const { analysis } = await API.get(
          "analyses",
          `/getAnalysisById/${id}`
        );
        console.log("analyseObjects", analysis);
      } catch (error) {
        console.error(error);
      }
    },
    async getAnalysis() {
      try {

        const { analyseObjects } = await API.get(
          "analyses",
          "/getUserAnalysis"
        );
        console.log("analyseObjects", analyseObjects);
        this.usersAnalysis = analyseObjects;
        for (let i = 0; i < analyseObjects.length; i++){
            if (this.analyseId === analyseObjects[i].id) {
                this.updated_by = analyseObjects[i].updated_by
                this.description = analyseObjects[i].description
                this.title = analyseObjects[i].title
            }
        }
      } catch (error) {
        console.error(error);
      }
    }
  },

  mounted() {
    this.getAnalysisById(this.analyseId);
    this.getAnalysis()
  },
};
</script>
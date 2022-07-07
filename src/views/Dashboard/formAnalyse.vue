<template>
  <div>
    <router-link to="/">Back to home</router-link>
    <v-form ref="form" lazy-validation>
      <v-text-field v-model="title" label="Name" required></v-text-field>

      <v-textarea
        v-model="description"
        label="description"
        required
      ></v-textarea>
    </v-form>
    <v-btn @click="updateAnalyse">{{
        hasData ? "Editer" : "Créer"
      }}</v-btn>
  </div>
</template>

<script>
import { API } from "aws-amplify";

export default {
  data() {
    return {
      description: this.description ?? null,
      title: this.title ?? null,
      analyseId: window.location.href.split("/:")[1],
      hasData: false,
      updated_by: null
    };
  },

  methods: {
    isUpdate() {
      if (this.description || this.title) {
        this.hasData = true;
      }
    },

    async updateAnalyse() {
      console.log("Update analyse started");
      try {
        console.log("Create Analyse started");

        const options = {
          body: {
            analyse_id: this.analyseId,
            title: this.title,
            description: this.description,
            updatedBy: this.updated_by
          },
        };
        await API.post("analyses", "/updateAnalyse", options);
        console.log(options)
        this.$router.push({ path: `/` });
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
            }
        }
        console.log(analyseObjects[1])
      } catch (error) {
        console.error(error);
      }
    }
  },

  mounted() {
    console.log(this.analyseId);
    this.getAnalysisById(this.analyseId);
    this.isUpdate();
    this.getAnalysis()
  },
};
</script>
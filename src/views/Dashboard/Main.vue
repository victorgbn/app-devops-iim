<template>
  <v-container>
    <h1>Hello !</h1>
    <v-btn @click="createAnalyses">Create Analyse</v-btn>

    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">ID</th>
            <th class="text-left">title</th>
            <th class="text-left">description</th>
            <th class="text-left">transcript</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in usersAnalysis" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.title }}</td>
            <td>{{ item.description }}</td>
            <td>{{ item.transcript }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-container>
</template>
<script>
import { API } from "aws-amplify";

export default {
  data() {
    return {
      usersAnalysis: null,
    };
  },
  methods: {
    async createAnalyses() {
      try {
        console.log("Create Analyse started");
        const response = await API.post("analyses", "/createAnalyses");
        this.$router.push({ path: `/formAnalyse/:${response.analyseId}` });
      } catch (e) {
        console.log(e);
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
      } catch (error) {
        console.error(error);
      }
    },
  },
  mounted() {
    this.getAnalysis();
  },
};
</script>

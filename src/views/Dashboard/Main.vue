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
            <th class="text-left">etat</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in usersAnalysis" :key="item.id">
              <td>
                <router-link :to="'/formAnalyse/:id'+item.id">
                  {{ item.id }}
                </router-link>
              </td>
              <td>{{ item.title ?? 'N/A' }}</td>
              <td>{{ item.description ?? 'N/A' }}</td>
              <td>{{ item.transcript ?? 'N/A' }}</td>
              <td style="color:white;" :style="!item.title || !item.description ? 'background:darkred;' : 'background:darkgreen'">{{ !item.title || !item.description ? 'Non paramétré' : 'Disponible' }}</td>
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

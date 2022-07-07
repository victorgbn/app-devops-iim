<template>
  <v-container>
    <h1>Hello !</h1>
    <v-btn @click="createAnalyses">Create Analyse</v-btn>

    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">ID</th>
            <th class="text-left">Titre</th>
            <th class="text-left">Description</th>
            <th class="text-left">Statut</th>
            <th class="text-left">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in usersAnalysis" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.title }}</td>
            <td>{{ item.description }}</td>
            <td style="color:white;" :style="item.description || item.title ? 'background:darkgreen' : 'background:darkorange'">{{ item.description || item.title ? 'Disponible' : 'En création' }}</td>
            <td style="cursor:pointer;">
              <a :href="'formAnalyse/:'+item.id">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="16" viewBox="0 0 24 24"><path d="M7.127 22.562l-7.127 1.438 1.438-7.128 5.689 5.69zm1.414-1.414l11.228-11.225-5.69-5.692-11.227 11.227 5.689 5.69zm9.768-21.148l-2.816 2.817 5.691 5.691 2.816-2.819-5.691-5.689z"/></svg>
              </a>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    <v-img :src='urlImage' />
  </v-container>
</template>
<script>
import { API, Storage } from "aws-amplify";

export default {
  data() {
    return {
      usersAnalysis: null,
      urlImage: ''
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
    }
  },
  async mounted() {
    this.getAnalysis();
    this.urlImage = await Storage.get('image1.jpeg')
  },
};
</script>
<template>
  <div>
    <router-link to="/">Back to home</router-link>
    <v-form ref="form" lazy-validation @click="updateAnalyse">
      <v-text-field v-model="title" label="Name" required></v-text-field>

      <v-textarea
        v-model="description"
        label="description"
        required
      ></v-textarea>

      <v-btn color="success" class="mr-4" type="submit">{{ update ? 'Enregistrer' : 'Créer' }}</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      description: this.description ?? null,
      title: this.title ?? null,
      analyseId: window.location.href.split('/:')[1],
      update: false
    };
  },

  methods: {
    updateAnalyse() {
      console.log('Update analyse started');
    },
    isUpdate() {
      if (this.description || this.title) { this.update = true }
    }
  },

  mounted() {
    console.log(this.analyseId);
    this.isUpdate();
  }
};
</script>
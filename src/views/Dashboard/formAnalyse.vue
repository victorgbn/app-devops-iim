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

      <v-btn color="success" class="mr-4" type="submit">Validate</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      description: this.description ?? null,
      title: this.title ?? null,
      analyseId: window.location.href.split('/:')[1]
    };
  },

  methods: {
    updateAnalyse() {
      console.log('Update analyse started');
    },
  },

  mounted() {
    console.log(this.analyseId);
  }
};
</script>
<template>
  <v-app>
    <amplify-authenticator>
      <v-main>
        <amplify-sign-out></amplify-sign-out>
      </v-main>
    </amplify-authenticator>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>

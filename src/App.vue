<template>
  <v-app>
    <amplify-authenticator>
      <v-main>
        <router-view></router-view>
        <amplify-sign-out></amplify-sign-out>
      </v-main>
    </amplify-authenticator>
    <p>Dev by Théo Popelin, Valentin Waché De Corbie, Victor Cabot et Victor Gaubin.</p>
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

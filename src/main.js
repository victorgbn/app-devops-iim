import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import {
  applyPolyfills,
  defineCustomElements,
} from '@aws-amplify/ui-components/loader';

import { Amplify } from 'aws-amplify';
import awsconfig from './aws-exports';

Amplify.configure(awsconfig);

applyPolyfills().then(() => {
  defineCustomElements(window);
});

Vue.config.ignoredElements = [/amplify-\w*/];

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueFormWizard from "vue-form-wizard";
import "vue-form-wizard/dist/vue-form-wizard.min.css";
import VueFormulate from "@braid/vue-formulate";
import ThemifyIcon from "vue-themify-icons";

Vue.config.productionTip = false;
Vue.use(VueFormWizard);
Vue.use(VueFormulate);
Vue.use(ThemifyIcon);

new Vue({
   router,
   render: (h) => h(App)
 }).$mount("#app");

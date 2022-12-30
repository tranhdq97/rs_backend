import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import i18n from "./i18n";
import vueClickOutsideElement from "vue-click-outside-element";

import "./assets/styles/main.scss";

createApp(App)
  .use(i18n)
  .use(store)
  .use(router)
  .use(vueClickOutsideElement)
  .mount("#app");

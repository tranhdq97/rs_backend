import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import i18n from "./i18n";
import axios from "axios";
import VueCookies, { useCookies } from "vue3-cookies";
import vueClickOutsideElement from "vue-click-outside-element";

import authAxios from "./axios";
import "./assets/styles/main.scss";
import { EToken } from "./enums/common";
import { ESAuth } from "./enums/store";
import { ERouter } from "./enums/routers";

const { cookies } = useCookies();

//Unauthenticated Axios Configurations
axios.interceptors.request.use(
  function (config) {
    const time = new Date();
    config.headers.TimezoneOffset = -time.getTimezoneOffset() / 60;
    return config;
  },
  function (error) {
    alert(error.message);
    return Promise.reject(error);
  }
);
axios.interceptors.response.use(
  function (config) {
    return config.data;
  },
  function (error) {
    alert(error.message);
    return Promise.reject(error);
  }
);
//Authenticated Axios Configurations
authAxios.interceptors.request.use(
  function (config) {
    config.headers.timeDiff = new Date().getTimezoneOffset;
    config.headers.Authorization = "Bearer " + cookies.get(EToken.ACCESS);
    return config;
  },
  function (err) {
    alert(err.message);
    return Promise.reject(err);
  }
);
authAxios.interceptors.response.use(
  function (config) {
    return config.data;
  },
  async function (error) {
    if (error.response.status === 401) {
      if (cookies.get(EToken.REFRESH)) {
        await store.dispatch(ESAuth.A_REFRESH);
        if (cookies.get(EToken.ACCESS)) return authAxios(error.config);
      }
      store.commit(ESAuth.M_REMOVE_CURRENT_USER);
      router.push(ERouter.SIGNIN);
      return;
    }
    alert(error.message);
    return Promise.reject(error);
  }
);

createApp(App)
  .use(i18n)
  .use(store)
  .use(router)
  .use(vueClickOutsideElement)
  .use(VueCookies)
  .mount("#app");

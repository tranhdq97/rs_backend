import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import sideBar from "./modules/sideBar";

export default createStore({
  modules: {
    sideBar,
  },
  plugins: [createPersistedState()],
});

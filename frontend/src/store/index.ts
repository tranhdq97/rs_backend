import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import sideBar from "./modules/sideBar";
import menu from "./modules/menu";
import order from "./modules/order";
import order_item from "./modules/order_item";
import table from "./modules/table";
import bill from "./modules/bill";

export default createStore({
  modules: {
    sideBar,
    menu,
    order,
    order_item,
    table,
    bill,
  },
  plugins: [createPersistedState()],
});

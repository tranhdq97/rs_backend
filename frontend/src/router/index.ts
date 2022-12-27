import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import VSignUp from "@/views/VSignUp.vue";
import VSignIn from "@/views/VSignIn.vue";
import VHome from "@/views/VHome.vue";
import VSetting from "@/views/VSetting.vue";
import VTables from "@/views/VTables.vue";
import VTable from "@/views/VTable.vue";
import { ERouter, ERouterName } from "@/enums/routers";

const routes: Array<RouteRecordRaw> = [
  {
    path: ERouter.HOME,
    name: ERouterName.HOME,
    component: VHome,
  },
  {
    path: ERouter.SIGNUP,
    name: ERouterName.SIGNUP,
    component: VSignUp,
  },
  {
    path: ERouter.SIGNIN,
    name: ERouterName.SIGNIN,
    component: VSignIn,
  },
  {
    path: ERouter.SETTING,
    name: ERouterName.SETTING,
    component: VSetting,
  },
  {
    path: ERouter.TABLES,
    name: ERouterName.TABLES,
    component: VTables,
  },
  {
    path: ERouter.TABLE,
    name: ERouterName.TABLE,
    component: VTable,
  },
  // {
  //   path: "/about",
  //   name: "about",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  // },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

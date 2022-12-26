import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import VSignUp from "@/views/VSignUp.vue";
import VSignIn from "@/views/VSignIn.vue";
import VHome from "@/views/VHome.vue";
import VSetting from "@/views/VSetting.vue";
import VTables from "@/views/VTables.vue";
import { ERouter } from "@/enums/routers";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: ERouter.HOME,
    component: VHome,
  },
  {
    path: "/" + ERouter.SIGNUP,
    name: ERouter.SIGNUP,
    component: VSignUp,
  },
  {
    path: "/" + ERouter.SIGNIN,
    name: ERouter.SIGNIN,
    component: VSignIn,
  },
  {
    path: "/" + ERouter.SETTING,
    name: ERouter.SETTING,
    component: VSetting,
  },
  {
    path: "/" + ERouter.TABLES,
    name: ERouter.TABLES,
    component: VTables,
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

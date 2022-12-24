import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import SignUpView from "@/views/SignUpView.vue";
import SignInView from "@/views/SignInView.vue";
import HomeView from "@/views/HomeView.vue";
import { ERouter } from "@/enums/routers";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: ERouter.HOME,
    component: HomeView,
  },
  {
    path: "/" + ERouter.SIGNUP,
    name: ERouter.SIGNUP,
    component: SignUpView,
  },
  {
    path: "/" + ERouter.SIGNIN,
    name: ERouter.SIGNIN,
    component: SignInView,
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

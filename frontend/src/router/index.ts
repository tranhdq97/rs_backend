import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import VSignUp from "@/views/VSignUp.vue";
import VSignIn from "@/views/VSignIn.vue";
import VHome from "@/views/VHome.vue";
import VSetting from "@/views/VSetting.vue";
import VTables from "@/views/VTables.vue";
import VTable from "@/views/VTable.vue";
import { ERouter, ERouterName } from "@/enums/routers";
import { EToken } from "@/enums/common";
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();
const routes: Array<RouteRecordRaw> = [
  {
    path: ERouter.HOME,
    name: ERouterName.HOME,
    component: VHome,
    meta: {
      authRequired: true,
    },
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
    meta: {
      authRequired: true,
    },
  },
  {
    path: ERouter.TABLES,
    name: ERouterName.TABLES,
    component: VTables,
    meta: {
      authRequired: true,
    },
  },
  {
    path: ERouter.TABLE,
    name: ERouterName.TABLE,
    component: VTable,
    meta: {
      authRequired: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record?.meta.authRequired)) {
    if (!cookies.get(EToken.ACCESS)) {
      router.push(ERouter.SIGNIN);
    } else next();
  } else next();
});

export default router;

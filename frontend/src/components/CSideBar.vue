<template>
  <div class="container" v-show="!isSideBarHide">
    <div class="menu">
      <span class="material-icons" @click="toggleSideBar">menu</span>
      <span
        class="material-icons chevron-left"
        v-if="!isSideBarCollapsed"
        @click="collapseSideBar"
      >
        chevron_left
      </span>
    </div>
    <CSideBarSelector :title="ECommon.HOME" icon="home" />
    <CSideBarSelector
      :title="ECommon.TABLES"
      icon="chair"
      :to="ERouter.TABLES"
    />
    <div class="grow"></div>
    <CSideBarSelector
      :title="ECommon.SETTING"
      icon="settings"
      :to="ERouter.SETTING"
    />
    <CSideBarSelector
      :title="ECommon.SIGNOUT"
      icon="logout"
      :to="ERouter.SIGNIN"
    />
  </div>
</template>

<script lang="ts">
import { ECommon } from "@/enums/common";
import { ELanguageCodes } from "@/enums/languages";
import { ERouter, ERouterName } from "@/enums/routers";
import { ESSideBar } from "@/enums/store";
import { computed, defineComponent, watch, ref } from "vue";
import { useI18n } from "vue-i18n";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import CSideBarSelector from "./CSideBarSelector.vue";

export default defineComponent({
  components: { CSideBarSelector },
  setup() {
    const store = useStore();
    const router = useRouter();
    const isSideBarHide = ref(true);
    const isSideBarCollapsed = computed(
      () => store.getters[ESSideBar.G_IS_SIDEBAR_COLLAPSED]
    );
    const collapseSideBar = () => {
      store.dispatch(ESSideBar.A_COLLAPSE_SIDEBAR);
    };
    const toggleSideBar = () => {
      store.dispatch(ESSideBar.A_TOGGLE_SIDEBAR);
    };
    const { locale } = useI18n({ useScope: "global" });
    const initLocale = localStorage.getItem(ECommon.LOCALE);
    locale.value = initLocale ? initLocale : ELanguageCodes.VIETNAMESE;
    watch(
      () => router.currentRoute.value.name,
      (currentRoute) => {
        currentRoute === ERouterName.SIGNUP ||
        currentRoute === ERouterName.SIGNIN
          ? (isSideBarHide.value = true)
          : (isSideBarHide.value = false);
      }
    );
    return {
      ERouter,
      ECommon,
      isSideBarHide,
      isSideBarCollapsed,
      collapseSideBar,
      toggleSideBar,
    };
  },
});
</script>
<style lang="scss" scoped>
.container {
  height: 100vh;
  background: var(--c-primary);
  box-shadow: var(--bs-medium) 0 var(--bs-blur) var(--bs-color);
}
.grow {
  align-items: flex-start;
  flex-grow: 1;
}
.menu {
  width: 100%;
  padding: var(--s-small);
  justify-content: space-between;
  .material-icons:hover {
    color: var(--c-white);
  }
}
.chevron-left {
  font-weight: var(--fw-small);
  margin-right: -20px;
  background: var(--c-primary);
  border-radius: var(--s-small);
  box-shadow: var(--bs-medium) 0 1px var(--bs-color);
  z-index: 99;
  color: var(--c-white);
  &:hover {
    background: var(--c-primaryLight);
  }
}
</style>

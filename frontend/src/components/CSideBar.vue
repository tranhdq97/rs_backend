<script lang="ts">
import { ECommon } from "@/enums/common";
import { ELanguageCodes } from "@/enums/languages";
import { ERouter, ERouterName } from "@/enums/routers";
import { ESAuth, ESMenuType, ESSideBar } from "@/enums/store";
import { computed, defineComponent, watch, ref } from "vue";
import { useI18n } from "vue3-i18n";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import CSideBarSelector from "./CSideBarSelector.vue";

export default defineComponent({
  components: { CSideBarSelector },
  setup() {
    const store = useStore();
    const router = useRouter();
    const i18n = useI18n();
    const mediaQuery = window.matchMedia("(max-width: 480px)");
    const isSideBarCollapsed = ref(mediaQuery.matches);
    const initLocale = localStorage.getItem(ECommon.LOCALE);
    store.dispatch(ESMenuType.A_GET_MENU_TYPES);
    i18n.setLocale(initLocale ? initLocale : ELanguageCodes.VIETNAMESE);
    const staffTypeID = computed<number>(
      () => store.getters[ESAuth.G_USER]?.type?.id || -1
    );
    const isSideBarHide = ref(true);
    const isSideBarExpanded = computed(
      () => store.getters[ESSideBar.G_IS_SIDEBAR_COLLAPSED]
    );
    const isTablesNotAllowed = computed(() => {
      const notAllowedRoles = router.resolve(ERouter.TABLES);
      return (notAllowedRoles?.meta?.notAllowedRoles as []).some(
        (item) => item === staffTypeID.value || staffTypeID.value < 0
      );
    });
    const isStaffsNotAllowed = computed(() => {
      const notAllowedRoles = router.resolve(ERouter.STAFFS);
      return (notAllowedRoles?.meta?.notAllowedRoles as []).some(
        (item) => item === staffTypeID.value || staffTypeID.value < 0
      );
    });
    const isSettingNotAllowed = computed(() => {
      const notAllowedRoles = router.resolve(ERouter.SETTING);
      return (notAllowedRoles?.meta?.notAllowedRoles as []).some(
        (item) => item === staffTypeID.value || staffTypeID.value < 0
      );
    });
    const expandSideBar = () => {
      store.dispatch(ESSideBar.A_COLLAPSE_SIDEBAR);
    };
    const toggleSideBar = () => {
      if (mediaQuery.matches)
        isSideBarCollapsed.value = !isSideBarCollapsed.value;
      store.dispatch(ESSideBar.A_TOGGLE_SIDEBAR);
    };
    const signOut = () => {
      store.dispatch(ESAuth.A_SIGN_OUT);
      router.push(ERouter.SIGNIN);
    };
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
      mediaQuery,
      staffTypeID,
      isSideBarHide,
      isSideBarExpanded,
      isTablesNotAllowed,
      isStaffsNotAllowed,
      isSettingNotAllowed,
      isSideBarCollapsed,
      expandSideBar,
      toggleSideBar,
      signOut,
      router,
    };
  },
});
</script>

<template>
  <div class="container box-shadow" v-show="!isSideBarHide && staffTypeID > 0">
    <div class="menu">
      <span class="material-icons" @click="toggleSideBar">menu</span>
      <span
        class="material-icons chevron-left"
        v-if="!isSideBarExpanded && !mediaQuery.matches"
        @click="expandSideBar"
      >
        chevron_left
      </span>
    </div>
    <CSideBarSelector
      :title="ECommon.MENU"
      icon="menu_book"
      :to="ERouter.MENU"
      v-if="!isSideBarCollapsed"
    />
    <CSideBarSelector
      v-if="!isTablesNotAllowed && !isSideBarCollapsed"
      :title="ECommon.TABLES"
      icon="chair"
      :to="ERouter.TABLES"
    />
    <CSideBarSelector
      v-if="!isStaffsNotAllowed && !isSideBarCollapsed"
      :title="ECommon.STAFFS"
      icon="diversity_3"
      :to="ERouter.STAFFS"
    />
    <div class="grow" v-if="!isSideBarCollapsed"></div>
    <CSideBarSelector
      v-if="!isSettingNotAllowed && !isSideBarCollapsed"
      :title="ECommon.SETTING"
      icon="settings"
      :to="ERouter.SETTING"
    />
    <CSideBarSelector
      v-if="staffTypeID > 0 && !isSideBarCollapsed"
      :title="ECommon.SIGNOUT"
      icon="logout"
      :to="router.currentRoute.value.path"
      @click="signOut"
      :notActiveAllowed="true"
    />
  </div>
</template>

<style lang="scss" scoped>
.container {
  height: 100vh;
  background: var(--c-primary);
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
@media screen and (max-width: 480px) {
  .container {
    position: fixed;
    left: 0;
    z-index: 100;
    background: var(--c-primaryTransparent);
    height: fit-content;
  }
}
</style>

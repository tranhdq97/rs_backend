<template>
  <router-link
    :to="to"
    :class="
      'wrapper' +
      (notActiveAllowed ? ' not-allowed-active' : '') +
      (isNotAllowed ? ' disabled' : '')
    "
  >
    <span :class="'material-icons'">{{ icon }}</span>
    <div class="title" v-show="!isSideBarCollapsed">{{ $t(title) }}</div>
  </router-link>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useStore } from "vuex";
import { ESAuth, ESSideBar } from "@/enums/store";
import { useRouter } from "vue-router";
import { IFStaff } from "@/interfaces/staff";

export default defineComponent({
  props: {
    title: { type: String, required: true },
    icon: { type: String, required: true },
    to: { type: String, required: true },
    notActiveAllowed: { type: Boolean, required: false },
  },
  setup(props) {
    const store = useStore();
    const router = useRouter();
    const toRouter = router.getRoutes().find((item) => item.path === props.to);
    const notAllowedRoles = (toRouter?.meta?.notAllowedRoles as number[]) || [];
    const staff = computed<IFStaff>(() => store.getters[ESAuth.G_USER]);
    const isNotAllowed = computed(() => {
      const staffTypeID = staff.value?.type?.id || -1;
      return notAllowedRoles.some((item) => item === staffTypeID);
    });
    const isSideBarCollapsed = computed(
      () => store.getters[ESSideBar.G_IS_SIDEBAR_COLLAPSED]
    );
    return { isSideBarCollapsed, isNotAllowed };
  },
});
</script>

<style lang="scss" scoped>
.title {
  white-space: nowrap;
}
.wrapper {
  display: flex;
  padding: var(--s-small);
  justify-content: left;
  align-items: center;
  width: 100%;
  gap: var(--s-small);
  cursor: pointer;
  text-decoration: none;
  color: var(--c-text);
  &:hover {
    color: var(--c-white);
    span {
      color: var(--c-white);
    }
  }
}
.router-link-active {
  background: var(--c-primaryDark);
}
.not-allowed-active {
  background: var(--c-primary);
}
.disabled {
  span {
    color: var(--c-grey);
  }
}
</style>

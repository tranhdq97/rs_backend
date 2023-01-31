<template>
  <router-link
    :to="to"
    :class="'wrapper' + (activeNotAllowed ? ' not-allowed-active' : '')"
  >
    <span class="material-icons">{{ icon }}</span>
    <div class="title" v-show="!isSideBarCollapsed">{{ $t(title) }}</div>
  </router-link>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useStore } from "vuex";
import { ESSideBar } from "@/enums/store";
import { useRouter } from "vue-router";
import { ERouter } from "@/enums/routers";

export default defineComponent({
  props: {
    title: { type: String, required: true },
    icon: { type: String, required: true },
    to: { type: String, default: ERouter.HOME },
    activeNotAllowed: { type: Boolean, default: false },
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const isSideBarCollapsed = computed(
      () => store.getters[ESSideBar.G_IS_SIDEBAR_COLLAPSED]
    );
    return { isSideBarCollapsed, router };
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
</style>
